
NUM_EPOCH = 180
NUM_BATCH_PER_EPOCH = NUM_EXAMPLES_PER_EPOCH_FOR_TRAIN // BATCH_SIZE
ckpt_dir = './model/'

# train
saver = tf.train.Saver()
with tf.Session() as sess:
    ckpt = tf.train.get_checkpoint_state(ckpt_dir)
    if (ckpt and ckpt.model_checkpoint_path):
        saver.restore(sess, ckpt.model_checkpoint_path)
    # assume the name of checkpoint is like '.../model.ckpt-1000'
        gs = int(ckpt.model_checkpoint_path.split('/')[-1].split('-')[-1])
        sess.run(tf.assign(global_step, gs))
    else:
    # no checkpoint found
        sess.run(tf.global_variables_initializer())
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(sess=sess, coord=coord)
    loss = []
    for i in range(NUM_EPOCH):
        _loss = []
        for _ in range(NUM_BATCH_PER_EPOCH):
            l, _ = sess.run([total_loss, train_op])
            _loss.append(l)
        loss_this_epoch = np.sum(_loss)
        gs = global_step.eval()
        print('loss of epoch %d: %f' % (gs / NUM_BATCH_PER_EPOCH, loss_this_epoch))
        loss.append(loss_this_epoch)
        saver.save(sess, ckpt_dir + 'model.ckpt', global_step=gs)
    coord.request_stop()
    coord.join(threads)

    print('Done')

