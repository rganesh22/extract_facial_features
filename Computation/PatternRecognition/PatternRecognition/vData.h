#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

typedef struct
{
	int x;
	int y;
}point;

typedef struct
{
	int x;
	int y;
	int w;
	int h;
}vobject;

class vData; 

point vobjectToPoint(vobject obj);

class vData{
		string fileContent;
		vector<string> fileContentV;
		string fileLocation;

		vector<point> facedeltas;

		vector<vobject>l_eye;
		vector<vobject>r_eye;

		vector<vobject>nose;
		vector<vobject>mouth;

		vector<vobject>face;

	    vector<point>l_pupil;
		vector<point>r_pupil;
	public:
		//set
		void setFileLocation(string fileLocation);
		void setFileContent();

		void set_l_eye(vector<vobject>& pts);
		void set_r_eye(vector<vobject>& pts);

		void set_nose(vector<vobject>& pts);
		void set_mouth(vector<vobject>& pts);

		void set_face(vector<vobject>& pts);

		void set_l_pupil(vector<point>& pts);
		void set_r_pupil(vector<point>& pts);

		void set_face_deltas(vector<point>& pts);
		
		vector<string> getfileContentV();

		//get
		string getFileLocation();
		string getFileContent();

		vector<vobject> get_l_eye();
		vector<vobject> get_r_eye();

		vector<vobject> get_nose();
		vector<vobject> get_mouth();

		vector<vobject> get_face();

		vector<point> get_l_pupil();
		vector<point> get_r_pupil();

		vector<point> get_face_deltas();
		//other
};

void parsePts(vData& vd);

void computeDeltas(vData& vd, vector<vobject>& pts);

void write_vec(const vector<string>& vec);

point subtractPts(point one, point two);

vector<point> subtractPointVectors(vector<point>& one, vector<point>& two);


