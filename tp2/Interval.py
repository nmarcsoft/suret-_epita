from Expression import *
from Program import *
from Domain import *
from Visiteur import *

class Interval(Domain):
    def __init__(self, domain):
        self.dom = domain
        
    def upperBound(self, s2):
        for key in self.domain:
            if key in s2:
                self.domain[key] = (min(self.domain[key][0],s2[key][0]) , max(self.domain[key][1],s2[key][1]))
        return self.domain
        
    def lowerBound(self, s2):
        for key in self.domain:
            if key in s2:
                self.domain[key] = (max(self.domain[key][0],s2[key][0]) , min(self.domain[key][1],s2[key][1]))
        return self.domain

class VisiteurInterval(VisiteurNonRel):
    def __init__(self, dom):
        self.dom = dom.copy()
        
    def sameVisiteur(self, domain):
        return VisiteurInterval(domain)
        
    def upperBound(self, d1, d2):
        return d1.upperBound(d2)
        
    def visitVar(self, var):
        return self.dom[var.variable]
        
    def visitCst(self, cst):
        return (cst.integer, cst.integer)

    def visitPlus(self, plus):
        pass

    def visitDiff(self, diff):
        pass

    def visitEq(self, eq):
        pass

    def visitInf(self, inf):
        pass

    def visitNeg(self, neg):
        abstractEvaluation = neg.bExp.abstractEvaluation(self)
        res = set()
        for elm in abstractEvaluation:
            res.add(not elm)
        return res

    def visitPostAssertEq(self, bExp):
        leftAbstractEvaluation = bExp.left.abstractEvaluation(self)
        rightAbstractEvaluation = bExp.right.abstractEvaluation(self)
        bExp.left.postAssert(self,rightAbstractEvaluation)
        bExp.right.postAssert(self,leftAbstractEvaluation)
        return self.dom

    def visitPostAssertInf(self, bExp):
        pass

    def visitPostAssertPlus(self, plus, domain):
        pass

    def visitPostAssertDiff(self, diff, domain):
        pass
