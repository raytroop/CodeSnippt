protobuf:
	protoc lm.helloworld.proto -I. --cpp_out=.
writer:
	g++ lm.helloworld.pb.cc writer.cpp  -I. -lprotobuf -o writer
reader:
	g++ lm.helloworld.pb.cc reader.cpp  -I. -lprotobuf -o reader