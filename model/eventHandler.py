from pygame.event import get


class EventHandler:
    def __init__(self, *super_event_type):
        self.events = {}
        self.sub_events_dict = {}
        for se in super_event_type:
            self.sub_events_dict[se] = {}
            self.events[se] = \
                lambda event: self.sub_events_dict[se].get(event.key, lambda: None)()

    def add_event(self, event_type, event=lambda: None):
        '''
        :param event_type(int): super event that have not any sup event (QUIT).
        :param event(int): action that must happen in lambda like (lambda event: sys.exit(0)).
        :return: None
        '''
        self.events[event_type] = event

    def add_subevent(self, super_event_type, sub_event_key, event=lambda: None):
        '''
        :param event_type(int): super event (KEYDOWN, KEYUP, ..).
        :param key(int): sub event from this super event (K_LEFT, K_RIGHT, K_ESC, K_A, ...).
        :param event: what happen when thtat event occure, it must be callable attribute
                            like function object or lambda (sys.exit).
        :return: None
        '''
        self.sub_events_dict[super_event_type][sub_event_key] = event

    def check_events(self):
        for event in get():
            self.events.get(event.type, lambda x: None)(event)
