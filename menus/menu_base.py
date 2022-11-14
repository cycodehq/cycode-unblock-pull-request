from abc import abstractmethod, ABC


class MenuBase(ABC):
    def menu_chosen(self, answers):
        return answers.get('menu') == self.get_menu()

    @abstractmethod
    def get_menu(self):
        pass

    @abstractmethod
    def handle(self, answers):
        pass