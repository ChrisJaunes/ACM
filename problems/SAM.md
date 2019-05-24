# 后缀自动机及广义SAM测试

| Prob                                                         | Result  | Time    | Memory   | author | note                                                         |
| :----------------------------------------------------------- | :------ | ------- | -------- | ------ | ------------------------------------------------------------ |
| [POJ1509](<http://poj.org/problem?id=1509>)                  | AC      | 0 MS    | 2936 KB  | HJJ    |                                                              |
| [SPOJNSUBSTR](<https://vjudge.net/problem/SPOJ-NSUBSTR>)     | AC      | 120 MS | 137216 KB | HJJ    | string会T                                                    |
| [SPOJ-SUBLEX](<https://vjudge.net/problem/SPOJ-SUBLEX>)      | AC      | 80MS | 59392 KB | HJJ    |                                                              |
| [SPOJ-LCS](<https://vjudge.net/problem/SPOJ-LCS>)            | AC      | 30 MS   | 70656 KB | HJJ    |                                                              |
| ~~[SPOJ-LCS2](<https://vjudge.net/problem/SPOJ-LCS2>)~~    | AC      | 150 MS  | 50176 KB | HJJ    | 重要！匹配成功时要考虑Right更小的匹配                        |
| ~~[SPOJ-LCS2](<https://vjudge.net/problem/SPOJ-LCS2>)~~  | AC      | 140 MS  | 40960 KB | HJJ    | 发现了一个巨大bug，已修正板子                                |
| [SPOJ-LCS2](<https://vjudge.net/problem/SPOJ-LCS2>)          | AC      | 80 MS  | 41984 KB | HJJ    | 已换了个板子                              |
| [HRY and Repeaters](source/2019-04-21_2019SCUT_SE_SchoolContest) | MLE(AC) | 1140 MS | 261 MB   | HJJ    |                                                              |
| [HRY and Repeaters](source/2019-04-21_2019SCUT_SE_SchoolContest) | AC      | 1076 MS | 255 MB   | HJJ    | vetcor耗空间                                                 |
| [USACO17DEC](<https://www.luogu.org/problemnew/show/P4081>)  | !AC     | 215MS   | 23224 KB | HJJ    | !单用SAM的做法很有意思，[题解](https://ctz45562.github.io/2019/04/27/%E6%B4%9B%E8%B0%B7-P4081-USACO17DEC-Standing-Out-from-the-Herd/) |
| [BZOJ3998](https://www.lydsy.com/JudgeOnline/problem.php?id=3998) | AC | 5648 MS | 124828 KB | HJJ |                                                              |
| [BZOJ3238](https://www.lydsy.com/JudgeOnline/problem.php?id=3238) | ！AC | 2036 MS | 120924 KB | HJJ |                                                              |
|                                                              |         |         |           |        |                                                              |
|                                                              |         |         |           |        |                                                              |
|                                                              |         |         |           |        |                                                              |

待测试：

BZOJ2555

USACO17DEC

POJ2752

[M - Mediocre String Problem](https://codeforces.com/gym/101981/problem/M)

BZOJ3926

POJ1743

[BZOJ3238](https://www.lydsy.com/JudgeOnline/problem.php?id=3238)