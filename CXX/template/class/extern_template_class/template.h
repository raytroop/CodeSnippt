template<typename T>
class Blob
{
public:
	Blob(): _a(0) {}
	Blob(T a): _a(a) {}
private:
	T _a;
};

template<typename T>
bool compare(const T& a, const T& b)
{
	return a > b;
}