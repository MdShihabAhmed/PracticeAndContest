#include <iostream>
#include <fstream>

using std::cout;
using std::endl;

int main() {
	std::ifstream read("race.in");
	int k;
	int n;
	read >> k >> n;

	std::ofstream written("race.out");
	for (int q = 0; q < n; q++) {
		int x;
		int unspeed = 0, total = 0;
		int result = 0;
		read >> x;
		for(int speed = 1;;speed++){
			if (speed>x){
				unspeed = speed - 1;
				total+=unspeed;
				result++;
				if(total>=k){
					break;
				}
			}
			total+=speed;
			result++;

			if(total>=k){
				break;
			}
		}
		written << result << '\n';
	}
}