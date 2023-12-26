import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('result/cfg1/log.csv')

train_loss = df['train_loss'] # train loss 데이터
valid_loss = df['val_loss']  # validation loss 데이터


plt.plot(range(163), train_loss, label='Train Loss')
plt.plot(range(163), valid_loss, label='Validation Loss')
plt.title('Train and Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

plt.show()
