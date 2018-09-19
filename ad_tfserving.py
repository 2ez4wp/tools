#!/usr/bin/python
# encoding: utf-8

import os
import tensorflow as tf
workroot = "ad_model/20180807"
model_name = "model"
meta_file = workroot+"/"+model_name+".ckpt.meta"
ckpt_file = workroot+"/"+model_name+".ckpt"
export_path = workroot+"/tf-serving-model"

if __name__ == "__main__":
    saver = tf.train.import_meta_graph(meta_file)
    print("Loading saved model...")
    with tf.Session() as sess:
        saver.restore(sess, ckpt_file)
        x = sess.graph.get_tensor_by_name("x:0")
        prob = sess.graph.get_tensor_by_name("softmax:0")
        print(x)
        print(prob)
        builder = tf.saved_model.builder.SavedModelBuilder(export_path)
        tensor_info_x = tf.saved_model.utils.build_tensor_info(x)
        tensor_info_pro = tf.saved_model.utils.build_tensor_info(prob)
        signature_def_map = {
            "predict_image": tf.saved_model.signature_def_utils.build_signature_def(
                 inputs={"image": tensor_info_x},
                 outputs={"pro": tensor_info_pro},
                 method_name=tf.saved_model.signature_constants.PREDICT_METHOD_NAME
             )}
        builder.add_meta_graph_and_variables(sess,
                                            [tf.saved_model.tag_constants.SERVING],
                                            signature_def_map=signature_def_map)
        builder.save()
        print('builder.save finished.')
        #output_graph_def=tf.graph_util.convert_variables_to_constants(sess,input_graph_def=sess.graph_def,output_node_names=["prob"])
        #with tf.gfile.FastGFile(pb_file_path, mode='wb') as f:
            #f.write(output_graph_def.SerializeToString())
