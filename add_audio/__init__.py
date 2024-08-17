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
    note[name] = value + "[sound:SigmaRuleSong.mp3]"
    mw.col.update_note(note)


# create a new menu item, "test"
action_front = QAction("Add pronouncion front", mw)
# set it to call testFunction when it's clicked
qconnect(action_front.triggered, testFunction)
# and add it to the tools menu
mw.form.menuqt_accel_view.addAction(action_front)
mw.form.centralwidget.addAction(action_front)



