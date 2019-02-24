#include "vData.h"


point vobjectToPoint(vobject obj){
	point p;
	p.x = obj.x;
	p.y = obj.y;
	return p;
}


/*
	For vData object
*/
//file location
void vData::setFileLocation(string fileLocation){
	vData::fileLocation = fileLocation;
}

string vData::getFileLocation(){
	return vData::fileLocation;

}


//file content
void vData::setFileContent(){
	ifstream file(vData::fileLocation);
	string line;
	string content;
	cout << vData::fileLocation << endl;
	if (file.is_open()){
		while (getline(file, line)) {
			content += line;
			vData::fileContentV.push_back(line);
		}
		file.close();
	}else{
		cout << "File Cannot Be Opened" << endl;
	}

	vData::fileContent = content;
}

string vData::getFileContent(){
	return fileContent;
}

void vData::set_l_eye(vector<vobject>& pts){
	l_eye = pts;
}

vector<vobject> vData::get_l_eye(){
	return l_eye;
}

void vData::set_r_eye(vector<vobject>& pts){
	r_eye = pts;
}

vector<vobject> vData::get_r_eye(){ 
	return r_eye;
}

void vData::set_mouth(vector<vobject>& pts){
	mouth = pts;
}

vector<vobject> vData::get_mouth(){
	return mouth;
}

void vData::set_nose(vector<vobject>& pts){
	nose = pts;
}

vector<vobject> vData::get_nose(){
	return nose;
}

void vData::set_face(vector<vobject>& pts){
	face = pts;
}

vector<vobject> vData::get_face(){
	return face;
}

void vData::set_l_pupil(vector<point>& pts){
	l_pupil = pts;
}

vector<point> vData::get_l_pupil(){
		return l_pupil;
}

void vData::set_r_pupil(vector<point>& pts){
	r_pupil = pts;
}


vector<point> vData::get_r_pupil(){
	return r_pupil;
}


vector<string> vData::getfileContentV(){
	return fileContentV;
}

vector<point> vData::get_face_deltas(){
	return vData::facedeltas;
}

void vData::set_face_deltas(vector<point>& pts){
	vData::facedeltas = pts;
}


/*
	Other
*/

//s2p
void parsePts(vData& vd){

	vector<vobject> l_eye_pts;
	vector<vobject> r_eye_pts;
	vector<vobject> nose_pts;
	vector<vobject> mouth_pts;
	vector<vobject> face_pts;

	vector<point> l_pupil_pts;
	vector<point> r_pupil_pts;
	
	for (int i = 0; i < vd.getfileContentV().size(); i++){
		cout << (i * 100) / vd.getfileContentV().size() << endl;
		string line = vd.getfileContentV()[i];
		vobject vtemp;
		point ptemp;
		
		if (line != ""){

			if (line.find("face") != string::npos){
				string x = line.substr(7, 4);
				vtemp.x = stoi(x);
				string y = line.substr(12, 4);
				vtemp.y = stoi(y);
				string w = line.substr(17, 4);
				vtemp.w = stoi(w);
				string h = line.substr(22, 4);
				vtemp.h = stoi(h);
				face_pts.push_back(vtemp);
			}

			if (line.find("nose") != string::npos){
				string x = line.substr(7, 4);
				vtemp.x = stoi(x);
				string y = line.substr(12, 4);
				vtemp.y = stoi(y);
				string w = line.substr(17, 4);
				vtemp.w = stoi(w);
				string h = line.substr(22, 4);
				vtemp.h = stoi(h);
				nose_pts.push_back(vtemp);
			}

			if (line.find("mouth") != string::npos){
				string x = line.substr(8, 4);
				vtemp.x = stoi(x);
				string y = line.substr(14, 4);
				vtemp.y = stoi(y);
				string w = line.substr(19, 4);
				vtemp.w = stoi(w);
				string h = line.substr(24, 4);
				vtemp.h = stoi(h);
				mouth_pts.push_back(vtemp);
			}

			if (line.find("eye[1]") != string::npos){
				string x = line.substr(9, 4);
				vtemp.x = stoi(x);
				string y = line.substr(14, 4);
				vtemp.y = stoi(y);
				string w = line.substr(19, 4);
				vtemp.w = stoi(w);
				string h = line.substr(24, 4);
				vtemp.h = stoi(h);
				l_eye_pts.push_back(vtemp);
			}

			if (line.find("eye[2]") != string::npos){
				string x = line.substr(9, 4);
				vtemp.x = stoi(x);
				string y = line.substr(14, 4);
				vtemp.y = stoi(y);
				string w = line.substr(19, 4);
				vtemp.w = stoi(w);
				string h = line.substr(24, 4);
				vtemp.h = stoi(h);
				r_eye_pts.push_back(vtemp);
			}

			if (line.find("pupil[1]") != string::npos){
				string x = line.substr(11, 4);
				ptemp.x = stoi(x);
				string y = line.substr(16, 4);
				ptemp.y = stoi(y);
				l_pupil_pts.push_back(ptemp);
			}

			if (line.find("pupil[2]") != string::npos){
				string x = line.substr(11, 4);
				ptemp.x = stoi(x);
				string y = line.substr(16, 4);
				ptemp.y = stoi(y);
				r_pupil_pts.push_back(ptemp);
			}
		}

	}
	
	vd.set_l_pupil(l_pupil_pts);
	vd.set_r_pupil(r_pupil_pts);

	vd.set_l_eye(l_eye_pts);
	vd.set_r_eye(r_eye_pts);

	vd.set_face(face_pts);
	vd.set_mouth(mouth_pts);
	vd.set_nose(nose_pts);

	cout << "Finished" << endl;
}

void computeDeltas(vData& vd,vector<vobject>& pts){
	vector<point> tempDeltas;

	for (int i = 0; i < pts.size(); i++){
		if (i + 1 >= pts.size()){
			break;
		}

		point p;
		p.x = pts[i].x - pts[i + 1].x;
		p.y = pts[i].y - pts[i + 1].y;
		tempDeltas.push_back(p);
	}

	vd.set_face_deltas(tempDeltas);

}

void write_vec(const vector<string>& vec) {
	for (vector<string>::const_iterator iter = vec.begin();
		iter != vec.end(); ++iter) {
		cout << *iter << endl;
	}
}

point subtractsPts(point one, point two){
	point difference;
	difference.x = one.x - two.x;
	difference.y = one.y - two.y;
	return difference;
}

vector<point> subtractPointVectors(vector<point>& one,vector<point>& two){
	vector<point> vc;
	for (int i = 0; i < one.size(); i++){
		point p;
		p.x = one[i].x - two[i].x;
		p.y = one[i].y - two[i].y;
		vc.push_back(p);
	}
	return vc;
}