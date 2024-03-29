from pysm import State


def test_states_all(complex_state_machine):

    sm = complex_state_machine
    sm.initialize()

    states = sm.states_all

    print(states)

    assert (
        len(states) == 4
    )  # Paused, Working, Working.Substate1, Working.Substate2


def test_get_state(complex_state_machine):

    sm = complex_state_machine

    # Add in a test state
    name = "TestState"
    test_state = State(name)
    sm.add_state(test_state)

    sm.initialize()

    state = sm.state_get_by_name(name)

    assert test_state == state

    assert state.name == name
