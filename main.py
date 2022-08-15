import numpy as np;
import matplotlib.pyplot as plt;

x = np.linspace(0, 9 ,1000);
y = x;
arg = np.linspace(0 ,2*np.pi, 1000);

x1 = 4.5 + 0.8 * np.cos(arg);
y1 = 3.0 + 0.8 * np.sin(arg);

plt.figure(figsize=(9 ,6), dpi= 1000);
plt.axhline(0, 0, 4, color = 'gray');
plt.axhline(2, 0, 4, color = 'w');
plt.axhline(4, 0, 4, color = 'w');
plt.axhline(6, 0, 4, color = 'gray');
plt.axvline(0, color = 'gray'  );
plt.axvline(9, color = 'gray');

plt.fill_between(x, 0, 2, color = 'g');
plt.fill_between(x, 2, 4, color = 'w');
plt.fill_between(x, 4, 6, color = (1, 0.6, 0.2));

plt.plot(x1, y1, color = 'b', lw = '6');
plt.plot(4.5, 3, 'b', marker = '.', ms = '16');

for j in range(24):
    arg = np.arange(0, 2*np.pi, 2*np.pi/24 );
    x3 = 4.5 + 0.7 * np.cos(arg);
    y3 = 3.0 + 0.7 * np.sin(arg);
    x4 = 4.5 + 0.1 * np.cos(arg);
    y4 = 3.0 + 0.1 * np.sin(arg);
    plt.plot([ x3[j], x4[j] ], [ y3[j], y4[j] ], "b-");
plt.ylim(0, 6);
plt.xlim(0, 9);
plt.xticks([]);
plt.yticks([]);
plt.tight_layout();
plt.title('Happy Indian Independence Day', size = 40, color = 'w');
plt.show();