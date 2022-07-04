class TodoList:
    def __init__(self, task_list):
        self.todo_list = task_list
        self.count = len(task_list)

    @property
    def undone_list(self):
        return list(filter(lambda item: not item['done'], self.todo_list))

    @property
    def done_list(self):
        return list(filter(lambda item: item['done'], self.todo_list))


todo_list = [
    {"id": 1, "title": "出门买菜做饭", "done": True},
    {"id": 2, "title": "锻炼20分钟", "done": False},
    {"id": 3, "title": "记单词30分钟", "done": False},
    {"id": 4, "title": "写作30分钟", "done": True},
    {"id": 5, "title": "冥想30分钟", "done": False},
]

todo = TodoList(todo_list)
if __name__ == '__main__':
    print(todo.todo_list)
    print(todo.done_list)
    print(todo.undone_list)
