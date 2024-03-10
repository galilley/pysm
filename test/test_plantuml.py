from test_simple_on_off import sm, state_on, state_off
import string


def test_plantuml():

    remove = string.whitespace
    mapping = {ord(c): None for c in remove}

    uml_expected = """
        @startuml
            sm:
        state sm {
            on:
            off:
            [*] --> on
            on --> off: off
            off --> on: on
        }
        @enduml
        """
    uml_expected = uml_expected.translate(mapping)
    uml = sm.to_plantuml().translate(mapping)

    assert uml == uml_expected


def test_plantuml_tooltips():

    from pathlib import Path

    def on_error(state, event):
        pass

    sm.add_transition(state_on, state_off, events=["error"], condition=on_error)
    uml = sm.to_plantuml()

    file = Path(on_error.__code__.co_filename).name
    line = on_error.__code__.co_firstlineno
    txt = "[[{" + f"{file}#{line}" + "}" + " on_error()]]"

    assert txt in uml
