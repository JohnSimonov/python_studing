def arithmetic_progression(position, start, difference):
	if position == 1:
		return start 
	return arithmetic_progression(position - 1, start, difference) + difference