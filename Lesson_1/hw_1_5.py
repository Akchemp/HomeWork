# Задание_5:
# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

proceeds = int(input("Enter proceeds: "))
spending = int(input("Enter spending: "))
if proceeds > spending:
    rentability = proceeds-spending
    rent = rentability/proceeds
    print(f"Great work. You have {rentability} rentability")
    worker = int(input("How many people work: "))
    print(f"{rentability/worker} for one worker")
elif proceeds == spending:
    print("Not bad")
else:
    print("Next time")

