class Computer:
    mainboard = None
    cpu = None
    memory = None
    hard_drive = None
    video_card = None
    case = None

    def __repr__(self) -> str:
        result = ''
        result += 'mainboard = {}\n'.format(self.mainboard)
        result += 'cpu = {}\n'.format(self.cpu)
        result += 'memory = {}\n'.format(self.memory)
        result += 'hard_drive = {}\n'.format(self.hard_drive)
        result += 'video_card = {}\n'.format(self.video_card)
        result += 'case = {}\n'.format(self.case)
        return result
