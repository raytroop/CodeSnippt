# http://blog.csdn.net/handsomekang/article/details/9712125
# 函数式编程的思想。
# 可以理解成绑定了一部分参数的函数。
# 作用就是少传参数，更短，更简洁。
# 我之前做的一段用户留存率的程序。
# 需求是这样子的，选择某一天，然后以这天为准，次日留存，3日留存，7日留存，14日留存，30日留存。
# 已有一个获取第几天后的函数

from datetime import datetime,timedelta  
def GetNextDay(baseday,n):  
    return str((datetime.strptime(str(baseday),'%Y-%m-%d')+timedelta(days=n)).date())  
# >>GetNextDay('2013-07-31',2)
# '2013-08-02'

# 按照常规做法，要获取这些“x日留存”的日期，需要
GetNextDay(selected_day,1)  
GetNextDay(selected_day,2)  
GetNextDay(selected_day,6)  
GetNextDay(selected_day,13)  
GetNextDay(selected_day,29)


# 可以看到，第一个参数都是一样的，一些东西如果是一样的，往往意味着可以简化，就跟之前博文的itemgetter一样。
# 这时候偏函数派上用途了。
import functools  
nday = functools.partial(GetNextDay,'2013-07-31')	# const '2013-07-31' assign selected_day
# 这样上面的的代码就可以简化成下面这样了。
nday(1)  # here n = 1
nday(2)  # here n = 2
nday(6)  
nday(13)  
nday(29) 


# Tuzki 2014-10-15 09:20发表 [回复] [引用] [举报]没看这个文章之前，我都是这么做的，这次学习了：
# nday = lambda:n : GetNextDay('2013-07-31',n)


# In [2]: def add2(a, b):
#    ...:     return a + b
#    ...: 

# In [3]: addb = functools.partial(add2, 11)	# 11 assign to a

# In [4]: addb
# Out[4]: functools.partial(<function add2 at 0x7fb1544f31e0>, 11)

# In [5]: addb(2) # here b = 2
# Out[5]: 13


## used in TensorFlow object detection API
# model_builder.py
def build(model_config, is_training, add_summaries=True):

# train.py 
model_fn = functools.partial(
      model_builder.build,
      model_config=model_config,
      is_training=True)		# now model_fn only need ONE argument--add_summaries

trainer.train(create_input_dict_fn, model_fn, train_config, master, task,
                FLAGS.num_clones, worker_replicas, FLAGS.clone_on_cpu, ps_tasks,
                worker_job_name, is_chief, FLAGS.train_dir)

# trainer.py
def train(create_tensor_dict_fn, create_model_fn, train_config, master, task,
          num_clones, worker_replicas, clone_on_cpu, ps_tasks, worker_job_name,
          is_chief, train_dir, graph_hook_fn=None):
  """Training function for detection models.

  Args:
    create_tensor_dict_fn: a function to create a tensor input dictionary.
    create_model_fn: a function that creates a DetectionModel and generates
                     losses.
    train_config: a train_pb2.TrainConfig protobuf.
    master: BNS name of the TensorFlow master to use.
    task: The task id of this training instance.
    num_clones: The number of clones to run per machine.
    worker_replicas: The number of work replicas to train with.
    clone_on_cpu: True if clones should be forced to run on CPU.
    ps_tasks: Number of parameter server tasks.
    worker_job_name: Name of the worker job.
    is_chief: Whether this replica is the chief replica.
    train_dir: Directory to write checkpoints and training summaries to.
    graph_hook_fn: Optional function that is called after the training graph is
      completely built. This is helpful to perform additional changes to the
      training graph such as optimizing batchnorm. The function should modify
      the default graph.
  """

  detection_model = create_model_fn()


# /home/raytroop/PycharmProjects/models-master/research/object_detection/builders/dataset_builder.py
# functools.partial(tf.data.TFRecordDataset, buffer_size=8 * 1000 * 1000)
# 
# tf.data.TFRecordDataset
# 	__init__(
#     		filenames,
#     		compression_type=None,
#     		buffer_size=None
# 			)