import matplotlib.pyplot as plt

months =["Jan", "Feb", "March", "April"]
sales =[89000,87000, 77000, 90000]

# plot() function is used for drawing the graphics in python
# plt.plot(x-axis, y-axis)
plt.plot(months, sales, label="Sales",color='red',marker='P',
         mec='b',mfc='y', ms=15 )
plt.xlabel("Months") # for x-axis label
plt.ylabel("Sales")  #for y-axis label
plt.title("Month Wise Sales")
plt.grid()
plt.legend()
plt.show()