import re, copy
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


class Worker:
    def __init__(self, number:int):
        self.number = number
        self.task = None
        self.time_remaining = None

    def __repr__(self):
        return 'Worker {}'.format(self.number)

    def busy(self) -> bool:
        return self.task is not None

    def work(self):
        if self.busy():
            self.time_remaining -= 1

            if self.time_remaining <= 0:
                completed_task = self.task
                self.task = None
                return completed_task
        return None

    def assign_task(self, task):
        self.task = task
        self.time_remaining = task.time_to_complete()


class Instruction:

    def __init__(self, name:str):
        self.name = name
        self.depends_on = []

    def __eq__(self, other):
        if other.name and other.name == self.name:
            return True
        return False

    def __repr__(self):
        return self.name

    def time_to_complete(self):
        return 60 + ALPHABET.find(self.name) + 1


class Instructions:
    def __init__(self, file_name:str):
        self.instructions = {}
        self.assigned_tasks = []
        for line in open(file_name):
            instruction_parts = re.search('Step (.*) must be finished before step (.*) can begin', line)
            depends_on_name = instruction_parts.group(1)
            instruction_name = instruction_parts.group(2)

            if depends_on_name not in self.instructions.keys():
                depends_on = Instruction(name=depends_on_name)
                self.instructions[depends_on_name] = depends_on
            else:
                depends_on = self.instructions[depends_on_name]

            if instruction_name not in self.instructions.keys():
                instruction = Instruction(name=instruction_name)
                self.instructions[instruction_name] = instruction
            else:
                instruction = self.instructions[instruction_name]

            instruction.depends_on.append(depends_on)

    def unblocked_tasks(self):
        unblocked = []
        for instruction in self.instructions.values():
            if len(instruction.depends_on) == 0 and instruction not in self.assigned_tasks:
                unblocked.append(instruction)
        return sorted(unblocked, key=lambda x: x.name)

    def step_order(self):
        instructions = copy.deepcopy(self.instructions)
        order = []
        while len(instructions) > 0:
            potential_steps = []
            for step in instructions.values():
                if len(step.depends_on) == 0:
                    potential_steps.append(step)

            selected_step = sorted(potential_steps, key=lambda x: x.name)[0]
            order.append(instructions.pop(selected_step.name).name)

            for step in instructions.values():
                try:
                    step.depends_on.remove(selected_step)
                except ValueError:
                    pass

        return order

    def complete_task(self, task):
        for step in self.instructions.values():
            try:
                step.depends_on.remove(task)
            except ValueError:
                pass
        self.instructions.pop(task.name)
        self.assigned_tasks.remove(task)

    def assign_task(self, task, worker):
        worker.assign_task(task)
        self.assigned_tasks.append(task)

    def construct(self, number_of_workers=1):
        workers = []
        seconds = 0
        for i in range(0, number_of_workers):
            workers.append(Worker(number=i))

        while len(self.instructions) > 0:
            seconds += 1
            available_tasks = self.unblocked_tasks()
            for worker in workers:
                if not worker.busy() and len(available_tasks) > 0:
                    self.assign_task(available_tasks.pop(0), worker)
                completed_task = worker.work()
                if completed_task:
                    self.complete_task(completed_task)

        print("Job took {} seconds".format(seconds))












