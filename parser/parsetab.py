
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND BATCH_SIZE BOOL CREATE DELIMITER EPOCH ESTIMATOR FLOAT FORMULA FORMULA_EXP INT LEARNING_RATE LOSS MODEL OPTIMIZER REGULARIZER SHUFFLE SQL TRAIN TRAINING_PROFILE TYPE USE VALIDATION_SPLIT WITH WORDexp : CREATE ESTIMATOR WORD TYPE WORD FORMULA FORMULA_EXP DELIMITER\n            | CREATE ESTIMATOR WORD TYPE WORD FORMULA FORMULA_EXP LOSS WORD DELIMITER\n            | CREATE ESTIMATOR WORD TYPE WORD FORMULA FORMULA_EXP LOSS WORD LEARNING_RATE FLOAT DELIMITER\n            | CREATE ESTIMATOR WORD TYPE WORD FORMULA FORMULA_EXP LOSS WORD LEARNING_RATE FLOAT OPTIMIZER WORD REGULARIZER WORD DELIMITERexp : CREATE TRAINING_PROFILE WORD WITH SQL DELIMITER\n                | CREATE TRAINING_PROFILE WORD WITH SQL AND VALIDATION_SPLIT FLOAT DELIMITER\n                | CREATE TRAINING_PROFILE WORD WITH SQL AND VALIDATION_SPLIT FLOAT BATCH_SIZE INT EPOCH INT DELIMITER\n                | CREATE TRAINING_PROFILE WORD WITH SQL AND VALIDATION_SPLIT FLOAT BATCH_SIZE INT EPOCH INT SHUFFLE BOOL DELIMITERexp : TRAIN WORD WITH TRAINING_PROFILE WORDexp : USE WORD DELIMITERexp : SQL DELIMITER'
    
_lr_action_items = {'CREATE':([0,],[2,]),'TRAIN':([0,],[4,]),'USE':([0,],[5,]),'SQL':([0,16,],[3,19,]),'$end':([1,8,14,20,22,26,30,32,37,41,46,47,],[0,-11,-10,-9,-5,-1,-6,-2,-3,-7,-8,-4,]),'ESTIMATOR':([2,],[6,]),'TRAINING_PROFILE':([2,13,],[7,17,]),'DELIMITER':([3,10,19,24,28,29,35,39,44,45,],[8,14,22,26,30,32,37,41,46,47,]),'WORD':([4,5,6,7,15,17,27,38,43,],[9,10,11,12,18,20,29,40,45,]),'WITH':([9,12,],[13,16,]),'TYPE':([11,],[15,]),'FORMULA':([18,],[21,]),'AND':([19,],[23,]),'FORMULA_EXP':([21,],[24,]),'VALIDATION_SPLIT':([23,],[25,]),'LOSS':([24,],[27,]),'FLOAT':([25,33,],[28,35,]),'BATCH_SIZE':([28,],[31,]),'LEARNING_RATE':([29,],[33,]),'INT':([31,36,],[34,39,]),'EPOCH':([34,],[36,]),'OPTIMIZER':([35,],[38,]),'SHUFFLE':([39,],[42,]),'REGULARIZER':([40,],[43,]),'BOOL':([42,],[44,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'exp':([0,],[1,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> exp","S'",1,None,None,None),
  ('exp -> CREATE ESTIMATOR WORD TYPE WORD FORMULA FORMULA_EXP DELIMITER','exp',8,'p_create_model','parser.py',35),
  ('exp -> CREATE ESTIMATOR WORD TYPE WORD FORMULA FORMULA_EXP LOSS WORD DELIMITER','exp',10,'p_create_model','parser.py',36),
  ('exp -> CREATE ESTIMATOR WORD TYPE WORD FORMULA FORMULA_EXP LOSS WORD LEARNING_RATE FLOAT DELIMITER','exp',12,'p_create_model','parser.py',37),
  ('exp -> CREATE ESTIMATOR WORD TYPE WORD FORMULA FORMULA_EXP LOSS WORD LEARNING_RATE FLOAT OPTIMIZER WORD REGULARIZER WORD DELIMITER','exp',16,'p_create_model','parser.py',38),
  ('exp -> CREATE TRAINING_PROFILE WORD WITH SQL DELIMITER','exp',6,'p_training_profile','parser.py',79),
  ('exp -> CREATE TRAINING_PROFILE WORD WITH SQL AND VALIDATION_SPLIT FLOAT DELIMITER','exp',9,'p_training_profile','parser.py',80),
  ('exp -> CREATE TRAINING_PROFILE WORD WITH SQL AND VALIDATION_SPLIT FLOAT BATCH_SIZE INT EPOCH INT DELIMITER','exp',13,'p_training_profile','parser.py',81),
  ('exp -> CREATE TRAINING_PROFILE WORD WITH SQL AND VALIDATION_SPLIT FLOAT BATCH_SIZE INT EPOCH INT SHUFFLE BOOL DELIMITER','exp',15,'p_training_profile','parser.py',82),
  ('exp -> TRAIN WORD WITH TRAINING_PROFILE WORD','exp',5,'p_train','parser.py',111),
  ('exp -> USE WORD DELIMITER','exp',3,'p_use_database','parser.py',121),
  ('exp -> SQL DELIMITER','exp',2,'p_SQL','parser.py',135),
]
