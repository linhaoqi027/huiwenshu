# huiwenshu
Tesla
采用两种方法解决。
- 方法一
利用不断增长的滑动窗口，两层循环来判断是否为回文数。在不考虑python自带的逆序函数的情况下，时间复杂度为O（n^2）
- 方法二
1.寻找中心点，2.考虑两种情况（回文数的唱的是奇数还是偶数）来判断以该中心点拓展的回文数的最大长度。时间复杂度为O（n^2）
