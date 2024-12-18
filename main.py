import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
from skfuzzy.control.visualization import FuzzyVariableVisualizer

ATTENDANCE = 'Attendance'
PERFORMANCE = 'Performance'
INTERNAL_MARKS = 'Internal Marks'
EXTERNAL_MARKS = 'External Marks'
POOR = 'Poor'
AVERAGE = 'Average'
GOOD = 'Good'
V_GOOD = 'Very Good'
EXCELLENT = 'Excellent'

def plot(antecedent, title):
    FuzzyVariableVisualizer(antecedent).view()[0].canvas.manager.set_window_title(title)
    
def set_parameters(antecedent, low, avg, good, v_good, excellent):
    antecedent[POOR] = fuzz.trapmf(antecedent.universe, low)
    antecedent[AVERAGE] = fuzz.trapmf(antecedent.universe, avg)
    antecedent[GOOD] = fuzz.trapmf(antecedent.universe, good)
    antecedent[V_GOOD] = fuzz.trapmf(antecedent.universe, v_good)
    antecedent[EXCELLENT] = fuzz.trapmf(antecedent.universe, excellent)

def fuzzy_generator(low_parameter, average_parameter, good_parameter, v_good_parameter, excellent_parameter):
	intrn_marks = ctrl.Antecedent(np.arange(0,105,5), INTERNAL_MARKS)
	attendance = ctrl.Antecedent(np.arange(0,105,5), ATTENDANCE)
	extrn_marks = ctrl.Antecedent(np.arange(0,105,5), EXTERNAL_MARKS)
	performance = ctrl.Consequent(np.arange(0,105,5), PERFORMANCE)
	
	set_parameters(intrn_marks, low_parameter, average_parameter, good_parameter, v_good_parameter, excellent_parameter)
	set_parameters(extrn_marks, low_parameter, average_parameter, good_parameter, v_good_parameter, excellent_parameter)
	set_parameters(performance, low_parameter, average_parameter, good_parameter, v_good_parameter, excellent_parameter)

	set_parameters(
    	attendance,
		[0, 0, 85, 85],
		[80, 85, 90, 95],
		[85, 90, 95, 100],
		[90, 95, 100, 100],
		[95, 100, 100, 100]
    )

	rules = [
		ctrl.Rule(attendance[POOR] & extrn_marks[POOR] & intrn_marks[POOR], performance[POOR]),
		ctrl.Rule(attendance[POOR] & extrn_marks[AVERAGE] & intrn_marks[POOR], performance[POOR]),
		ctrl.Rule(attendance[POOR] & extrn_marks[GOOD] & intrn_marks[POOR], performance[POOR]),
		ctrl.Rule(attendance[POOR] & extrn_marks[V_GOOD] & intrn_marks[POOR], performance[POOR]),
		ctrl.Rule(attendance[POOR] & extrn_marks[GOOD] & intrn_marks[V_GOOD], performance[POOR]),
		ctrl.Rule(attendance[POOR] & extrn_marks[POOR] & intrn_marks[AVERAGE], performance[POOR]),
		ctrl.Rule(attendance[POOR] & extrn_marks[AVERAGE] & intrn_marks[AVERAGE], performance[POOR]),
		ctrl.Rule(attendance[POOR] & extrn_marks[GOOD] & intrn_marks[AVERAGE], performance[POOR]),
		ctrl.Rule(attendance[POOR] & extrn_marks[GOOD] & intrn_marks[GOOD], performance[POOR]),
		ctrl.Rule(attendance[POOR] & extrn_marks[EXCELLENT] & intrn_marks[EXCELLENT], performance[POOR]),
		ctrl.Rule(attendance[POOR] & extrn_marks[EXCELLENT] & intrn_marks[GOOD], performance[POOR]),
		ctrl.Rule(attendance[AVERAGE] & extrn_marks[AVERAGE] & intrn_marks[GOOD], performance[AVERAGE]),
		ctrl.Rule(attendance[AVERAGE] & extrn_marks[GOOD] & intrn_marks[GOOD], performance[GOOD]),
		ctrl.Rule(attendance[AVERAGE] & extrn_marks[V_GOOD] & intrn_marks[GOOD], performance[GOOD]),
		ctrl.Rule(attendance[AVERAGE] & extrn_marks[V_GOOD] & intrn_marks[V_GOOD], performance[V_GOOD]),
		ctrl.Rule(attendance[AVERAGE] & extrn_marks[AVERAGE] & intrn_marks[EXCELLENT], performance[GOOD]),
		ctrl.Rule(attendance[AVERAGE] & extrn_marks[AVERAGE] & intrn_marks[AVERAGE], performance[AVERAGE]),
		ctrl.Rule(attendance[AVERAGE] & extrn_marks[POOR] & intrn_marks[POOR], performance[POOR]),
		ctrl.Rule(attendance[AVERAGE] & extrn_marks[POOR] & intrn_marks[GOOD], performance[AVERAGE]),
		ctrl.Rule(attendance[GOOD] & extrn_marks[AVERAGE] & intrn_marks[AVERAGE], performance[AVERAGE]),
		ctrl.Rule(attendance[GOOD] & extrn_marks[EXCELLENT] & intrn_marks[EXCELLENT], performance[V_GOOD]),
		ctrl.Rule(attendance[GOOD] & extrn_marks[GOOD] & intrn_marks[AVERAGE], performance[GOOD]),
		ctrl.Rule(attendance[GOOD] & extrn_marks[POOR] & intrn_marks[POOR], performance[POOR]),
		ctrl.Rule(attendance[V_GOOD] & extrn_marks[EXCELLENT] & intrn_marks[V_GOOD], performance[V_GOOD]),
		ctrl.Rule(attendance[V_GOOD] & extrn_marks[V_GOOD] & intrn_marks[V_GOOD], performance[V_GOOD]),
		ctrl.Rule(attendance[V_GOOD] & extrn_marks[POOR] & intrn_marks[POOR], performance[POOR]),
		ctrl.Rule(attendance[V_GOOD] & extrn_marks[GOOD] & intrn_marks[V_GOOD], performance[V_GOOD]),
		ctrl.Rule(attendance[V_GOOD] & extrn_marks[EXCELLENT] & intrn_marks[EXCELLENT], performance[EXCELLENT]),
		ctrl.Rule(attendance[EXCELLENT] & extrn_marks[EXCELLENT] & intrn_marks[V_GOOD], performance[V_GOOD]),
		ctrl.Rule(attendance[EXCELLENT] & extrn_marks[AVERAGE] & intrn_marks[AVERAGE], performance[V_GOOD]),
		ctrl.Rule(attendance[EXCELLENT] & extrn_marks[AVERAGE] & intrn_marks[V_GOOD], performance[GOOD]),
		ctrl.Rule(attendance[EXCELLENT] & extrn_marks[AVERAGE] & intrn_marks[GOOD], performance[GOOD]),
		ctrl.Rule(attendance[EXCELLENT] & extrn_marks[POOR] & intrn_marks[POOR], performance[POOR]),
		ctrl.Rule(attendance[EXCELLENT] & extrn_marks[AVERAGE] & intrn_marks[POOR], performance[AVERAGE]),
		ctrl.Rule(attendance[EXCELLENT] & extrn_marks[POOR] & intrn_marks[AVERAGE], performance[POOR]),
		ctrl.Rule(attendance[EXCELLENT] & extrn_marks[GOOD] & intrn_marks[POOR], performance[GOOD]),
		ctrl.Rule(attendance[EXCELLENT] & extrn_marks[POOR] & intrn_marks[GOOD], performance[AVERAGE]),
		ctrl.Rule(attendance[EXCELLENT] & extrn_marks[V_GOOD] & intrn_marks[POOR], performance[V_GOOD]),
		ctrl.Rule(attendance[EXCELLENT] & extrn_marks[POOR] & intrn_marks[V_GOOD], performance[AVERAGE]),
		ctrl.Rule(attendance[EXCELLENT] & extrn_marks[POOR] & intrn_marks[EXCELLENT], performance[GOOD]),
		ctrl.Rule(attendance[EXCELLENT] & extrn_marks[AVERAGE] & intrn_marks[EXCELLENT], performance[V_GOOD]),
		ctrl.Rule(attendance[EXCELLENT] & extrn_marks[GOOD] & intrn_marks[EXCELLENT], performance[V_GOOD]),
		ctrl.Rule(attendance[EXCELLENT] & extrn_marks[V_GOOD] & intrn_marks[EXCELLENT], performance[V_GOOD]),
		ctrl.Rule(attendance[EXCELLENT] & extrn_marks[EXCELLENT] & intrn_marks[EXCELLENT], performance[EXCELLENT]),
	]

	performance_ctrl = ctrl.ControlSystem(rules)
	perf_analysis = ctrl.ControlSystemSimulation(performance_ctrl)

	plot(intrn_marks, "Internal Marks")
	plot(attendance, "Attandance Marks")
	plot(extrn_marks, "External Marks")
	plot(performance, "Performance Marks")
	plt.show()

	def fuzzy(attend, intr_mark, extn_mark):
		perf_analysis.input[ATTENDANCE] = attend
		perf_analysis.input[EXTERNAL_MARKS] = extn_mark
		perf_analysis.input[INTERNAL_MARKS] = intr_mark

		perf_analysis.compute()

		return perf_analysis.output[PERFORMANCE]

	return fuzzy

low =       [0,  0, 60, 70]
average =   [50,60, 70, 80]
good =      [60,70, 80, 90]
v_good =    [70,80, 90, 100]
excellent = [80,90, 100,100]
compute = fuzzy_generator(low, average, good, v_good, excellent)

if __name__ == "__main__":
    while True:
        attendance, internal, external = map(int, input("Input marks (Attandance,Internal,External): ").split(","))
        print("Output :", str(compute(attendance, internal, external)))