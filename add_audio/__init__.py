from aqt import mw
from aqt.utils import showInfo, qconnect
from aqt.qt import *

def create_pronauncion() -> None:
    pass

def find_image() -> None:
    pass


def testFunction() -> None:
    card = mw.col.sched.getCard()
    if not card:
        showInfo("card not found")
        return
    note = card.note()
    name, value = note.items()[1]
    note[name] = value + "[sound:name.mp3]"
    mw.col.update_note(note)


action= QAction("Add pronouncion", mw)
qconnect(action.triggered, testFunction)
mw.form.menubar.addAction(action)



