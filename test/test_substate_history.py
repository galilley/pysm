import pytest
from pysm import State, StateMachine, Event


def test_substate_history(complex_state_machine):

    root = complex_state_machine
    root.initialize()

    # Retrieve states
    root.initialize()
    state_paused = root.state_get_by_name("Paused")
    state_working = root.state_get_by_name("Working")
    substate1 = root.state_get_by_name("Substate1")
    substate2 = root.state_get_by_name("Substate2")

    # Test UML highlighting of active.
    assert substate1.is_active
    uml = root.to_plantuml(highlight_active=True)
    assert "state Substate1 #line.bold;" in uml

    # Verify initialize called on_enter for all states on
    # path to initial leaf state.
    assert root.enter_called
    assert state_working.enter_called
    assert substate1.enter_called

    # Verify we start in correct state
    assert root.state == state_working
    assert root.leaf_state == substate1

    # Verify state path
    p = [root, state_working, substate1]
    assert root.state_path == p

    # Pause
    Event("pause")
    root.dispatch(Event("pause"))
    assert root.state == state_paused
    assert root.leaf_state == state_paused

    # Resume
    root.dispatch(Event("resume"))
    assert root.state == state_working
    assert root.leaf_state == substate1

    # Advance to second substate.
    root.dispatch(Event("step_complete"))
    assert root.state == state_working
    assert root.leaf_state == substate2

    # Verify state is_active properties
    assert root.is_active
    assert state_working.is_active
    assert substate2.is_active
    assert not substate1.is_active
    assert not state_paused.is_active

    # Test UML highlighting of active.
    uml = root.to_plantuml(highlight_active=True)
    assert "state Substate2 #line.bold;" in uml

    # Pause
    root.dispatch(Event("pause"))
    assert root.state == state_paused
    assert root.leaf_state == state_paused

    # Resume
    # Tests that history is working.
    root.dispatch(Event("resume"))
    assert root.state == state_working
    assert root.leaf_state == substate2

    # Back to first substate.
    root.dispatch(Event("step_complete"))
    assert root.state == state_working
    assert root.leaf_state == substate1

    # And check pause/resume again.
    root.dispatch(Event("pause"))
    root.dispatch(Event("resume"))
    assert root.state == state_working
    assert root.leaf_state == substate1


def test_event_reuse(complex_state_machine):

    # States
    root = complex_state_machine
    root.initialize()

    evt_pause = Event("pause")
    evt_resume = Event("resume")

    root.dispatch(evt_pause)
    root.dispatch(evt_resume)

    with pytest.raises(Exception):
        root.dispatch(evt_pause)


if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.DEBUG)
    test_substate_history()
