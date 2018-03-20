// rtp@ubuntu:~/test$ g++ -std=c++11 gflags.cpp  -lgflags
#include <gflags/gflags.h>
#include <iostream>
#include <string>
using namespace std;


DEFINE_string(model, "",
    "The model definition protocol buffer text file..");


int main(int argc, char* argv[])
{
	google::ParseCommandLineFlags(&argc, &argv, true);		// matching key-value
	cout << FLAGS_model << endl;
	cout << argc << endl;
	cout << string(argv[0]) << endl;
	cout << string(argv[1]) << endl;
	return 0;
}

// rtp@ubuntu:~/test$ ./a.out train --model="vgg"
// vgg
// 2
// ./a.out
// train



// DEFINE_string(gpu, "",
//     "Optional; run in GPU mode on given device IDs separated by ','."
//     "Use '-gpu all' to run on all available GPUs. The effective training "
//     "batch size is multiplied by the number of devices.");
// DEFINE_string(solver, "",
//     "The solver definition protocol buffer text file.");
// DEFINE_string(model, "",
//     "The model definition protocol buffer text file..");
// DEFINE_string(snapshot, "",
//     "Optional; the snapshot solver state to resume training.");
// DEFINE_string(weights, "",
//     "Optional; the pretrained weights to initialize finetuning, "
//     "separated by ','. Cannot be set simultaneously with snapshot.");
// DEFINE_int32(iterations, 50,
//     "The number of iterations to run.");
// DEFINE_string(sigint_effect, "stop",
//              "Optional; action to take when a SIGINT signal is received: "
//               "snapshot, stop or none.");
// DEFINE_string(sighup_effect, "snapshot",
//              "Optional; action to take when a SIGHUP signal is received: "
//              "snapshot, stop or none.");
