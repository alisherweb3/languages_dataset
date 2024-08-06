# languages_dataset

At the last code result will be
```
# Plot a pie chart of writing systems
plt.figure(figsize=(8, 8))
df_languages['Writing System'].value_counts().plot.pie(autopct='%1.1f%%', startangle=140, cmap='Set3')
plt.title('Distribution of Writing Systems')
plt.ylabel('')
plt.show()
```


<img src="/images/Screenshot_104.png">

We can see that latin enjoy it with 40,6%.
