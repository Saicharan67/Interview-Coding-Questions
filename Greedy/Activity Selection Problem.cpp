#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_set>
using namespace std;

struct Pair
{
	// stores start and finish time of the activities
	int start, finish;
};


void selectActivity(vector<Pair> activities)		// no-ref, no-const
{
	int k = 0;

	unordered_set<int> out;
	if (activities.size() > 0) {
		out.insert(0);
	}

	sort(activities.begin(), activities.end(),
		[](auto const &lhs, auto const &rhs) {
			return lhs.finish < rhs.finish;
		});

	for (int i = 1; i < activities.size(); i++)
	{

		if (activities[i].start >= activities[k].finish)
		{
			out.insert(i);
			k = i;			// update `i` as the last selected activity
		}
	}

	for (int i: out)
	{
		cout << "{" << activities[i].start << ", " << activities[i].finish
			 << "}" << endl;
	}
}

int main()
{
	vector<Pair> activities =
	{
		{1, 4}, {3, 5}, {0, 6}, {5, 7}, {3, 8}, {5, 9},
		{6, 10}, {8, 11}, {8, 12}, {2, 13}, {12, 14}
	};

	selectActivity(activities);

	return 0;
}