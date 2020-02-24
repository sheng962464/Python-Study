import time
import json
import pickle
#  如果作为参数的t未指定，将传入time.localtime()或者time.time()
"""
time.asctime([t])
作用：将struct_time类型的时间转换为如下形式：'Sun Jun 20 23:21:05 1993'
参数：struct_time类型或tuple类型的时间，不填参数的话默认为time.localtime()得到的时间。
返回值：'Sun Jun 20 23:21:05 1993'类型的时间。

time.ctime([secs])
作用：将时间戳的时间转换为表示本地时间的字符串。如果没有提供secs或没有提供secs，则使用time.time()返回的当前时间。
参数：时间戳类型的时间，如果不填默认为当前时间的时间戳。
返回值：格式化类型的时间，例如'Mon Mar 18 23:56:35 2019'。

time.gmtime([sec])
作用：将时间戳类型的时间转换为UTC中的struct_time，其中dst标志始终为零。时区转换。
参数：时间戳类型的时间，如果没有提供secs或没有提供secs，则使用time()返回的当前时间。
返回值：struct_time类型的时间

time.localtime([sec])
作用：就像time.gmtime()，但是转换为本地时间。当dst应用于给定的时间时，dst标志被设置为1。
参数：时间戳类型的时间，如果没有提供secs或没有提供secs，则使用time()返回的当前时间。
返回值：struct_time类型的时间

time.mktime(t)
作用：将struct_time类型的时间转换为时间戳类型。
参数：struct_time类型的时间。
返回值：时间戳类型。

time.monotonic()-->float
作用：返回一个单调时钟的值(以分数秒为单位)，即一个不能倒退的时钟。时钟不受系统时钟更新的影响。返回值的引用点是未定义的，因此只有连续调用的结果之间的差异是有效的。

time.monotonic_ns()-->int
作用：和time.monotonic()类似，但返回值为纳秒。

time.perf_counter()-->float
作用：返回性能计数器的值(以小数秒为单位)，即具有最高可用分辨率来测量短时间的时钟。它确实包括在睡眠期间所花费的时间，并且是全系统的。返回值的引用点是未定义的，因此只有连续调用的结果之间的差异是有效的。

time.perf_counter_ns()-->int
作用：和time.perf_counter()类似，但返回值为纳秒。

time.process_time()-->float
作用：返回当前进程的系统和用户CPU时间之和(以小数秒为单位)。它不包括睡眠时间。根据定义，它是过程范围的。返回值的引用点是未定义的，因此只有连续调用的结果之间的差异是有效的。

time.process_time_ns()-->int
作用：和time.process_time()类似，但返回值为纳秒。

time.sleep(secs)
作用：在给定的秒数内挂起调用线程的执行。
参数：秒数，参数可以是一个浮点数，表示更精确的睡眠时间。

time.strftime(format[,t])
作用：将struct_time类型的时间转换为format参数指定格式的字符串。
参数：

format:指定转换时间的字符串格式。
t:struct_time类型的时间，如果不填默认为当前时间（即time.localtime()返回的时间）
返回值：指定格式的字符串。

time.strptime(string[,format])
作用：根据格式解析表示时间的字符串。
参数：

string:字符串类型的时间。
format:提供字符串类型的时间的格式。
返回值：struct_time类型的时间。
注：format参数使用的指令与strftime()使用的指令相同;它默认为“%a %b %d %H:%M:%S %Y”，与ctime()返回的格式匹配。如果字符串不能按照格式进行解析，或者解析后有多余的数据，则会引发ValueError。当无法推断出更精确的值时，用于填充任何缺失数据的默认值是(1900、1、1、0、0、0、0、0、1、-1)。字符串和格式都必须是字符串。

time.time()-->float
作用：以秒为单位以浮点数返回历元之后的时间。

time.thread_time()-->float
作用：返回当前线程的系统和用户CPU时间之和(以小数秒为单位)。它不包括睡眠时间。它的定义是特定于线程的。返回值的引用点未定义，因此只有同一线程中连续调用的结果之间的差异是有效的。

time.thread_time_ns()-->int
作用：和time.thread_time()类似，但是返回值是纳秒。

time.time_ns()-->int
作用：和time.time()类似，但返回值是纳秒。
"""


"""
以下指令可以嵌入格式字符串中。它们显示时没有可选的字段宽度和精度规范。
%a-->星期的缩写
%A-->完整的星期的名称
%b-->月份的缩写
%B-->完整的月份名称
%c-->'Wed Mar 20 21:40:19 2019'格式
%d-->十进制数格式的日期[01,31]
%H-->小时（24小时制） 十进制数[00,23]
%I-->小时（12小时制） 十进制数[01,12]
%j-->一年中的一天（十进制数）[001,366]
%m-->月份（十进制数）[01,12]
%M-->分钟数（十进制数）[00,59]
%p-->AM或PM
%S-->秒数[00,59]
%U-->一年中的周数（星期日作为一周的第一天）十进制数[00,53],第一个星期日之前的所有日子被认为是第0周。
%w-->星期数（十进制数）[0,6]
%W-->一年中的周数（星期一作为一周的第一天）十进制数[00,53],第一个星期一之前的所有日子被认为是第0周。
%x-->日期表示（月/日/不带世纪的年份）例如'03/20/19'
%X-->时间表示（时:分:秒）例如'21:56:34'
%y-->不带世纪的年份(十进制数)[00,99]
%Y-->带世纪的年份(十进制数)
%z-->时区偏移指示与格式+ HHMM或-HHMM形式的UTC / GMT的正或负时差，其中H表示十进制小时数字，M表示小数分钟数字[-23：59，+ 23：59]。
%Z-->时区名称，例如'中国标准时间'
%%-->'%'字符。
"""

print('原Data数据结构：')
Data = time.localtime()
print(Data, type(Data))
print()

print('用json包转换：')
p_str_json = json.dumps(Data)
print(p_str_json, type(p_str_json))

mes_json = json.loads(p_str_json)
print(mes_json, type(mes_json))

print('json只能实现字符串和python内置结构的转换')
print()

print('用pickle包转换:')
p_str_pickle = pickle.dumps(Data)
print(p_str_pickle, type(p_str_pickle))

mes_pickle = pickle.loads(p_str_pickle)
print(mes_pickle, type(mes_pickle))

print('pickle能实现自定义类的保存')
print()


formatTime = time.strftime('%Y-%m-%d %H:%M:%S', Data)
print('格式化字符串:', formatTime)
print()

Data = time.time()
print(Data)
localData = time.localtime(Data)
print(localData)
mktimeData = time.mktime(localData)
print(mktimeData)
print()

print(time.asctime())
print(time.ctime())
print()

