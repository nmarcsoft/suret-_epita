from Sign import *

the = Affectation("x", DiffExp(CstExp(0),VarExp("x")))
ite = IfThenElse(InfTest(VarExp("x"),CstExp(0)),the,Program([]))
vis = VisiteurSigne({"x":{'+','0','-'}})
print(Program([ite]).accept(vis))

do = Affectation("x", DiffExp(VarExp("x"),CstExp(1)))
whil = While(InfTest(CstExp(0),VarExp("x")),do)
vis = VisiteurSigne({"x":{'+'}})
print(Program([whil]).accept(vis))
