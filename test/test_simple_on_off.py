from pysm import State, StateMachine, Event

state_on = State("on")
state_off = State("off")

sm = StateMachine("sm")
sm.add_state(state_on, initial=True)
sm.add_state(state_off)

sm.add_transition(state_on, state_off, events=["off"])
sm.add_transition(state_off, state_on, events=["on"])

sm.initialize()


def test():
    assert sm.state == state_on
    sm.dispatch(Event("off"))
    assert sm.state == state_off
    sm.dispatch(Event("on"))
    assert sm.state == state_on


if __name__ == "__main__":
    test()
