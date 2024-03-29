def test_states_all(complex_state_machine):

    sm = complex_state_machine
    states = sm.states_all

    print(states)

    assert (
        len(states) == 4
    )  # Paused, Working, Working.Substate1, Working.Substate2
