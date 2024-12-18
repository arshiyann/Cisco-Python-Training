@obj.route("/aboutus")

def f2():

  <h2><font color=green>About Us page</font></h2>
  return s

14

15 @obj.route("/mypage/<int:var>")

16 def f3 (var):

17

return f'<h2>var value is: (var)</h2>

18

19@obj.route("/dept/<mydept>")

20 def f4 (mydept):

21 if (mydept 'sales' or mydept qal):

22

return redirect(url_for('f2'))

23 else:

24

return redirect(url_for('f3',var-100))

25

26@obj.route("/news")

27 def £5():

28 return render template (display.html')

29

30

31 if name main

32 obj.run (debug=True)