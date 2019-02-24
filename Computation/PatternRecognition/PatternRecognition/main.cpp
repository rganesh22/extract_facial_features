#include "vData.h"



int main(){
	vData asdData;
	asdData.setFileLocation("E:\\BPR_2016\\ComputerVision\\tbp.vdata");
	asdData.setFileContent();
	parsePts(asdData);
	computeDeltas(asdData,asdData.get_face());

	vData nonasdData;
	nonasdData.setFileLocation("E:\\BPR_2016\\ComputerVision\\tbp.vdata");
	nonasdData.setFileContent();
	parsePts(nonasdData);
	computeDeltas(nonasdData, nonasdData.get_face());

	vData inputData;
	inputData.setFileLocation("E:\\BPR_2016\\ComputerVision\\tbp.vdata");
	inputData.setFileContent();
	parsePts(inputData);
	computeDeltas(inputData, inputData.get_face());

	vector<point> asdDifference = subtractPointVectors(asdData.get_face_deltas(), inputData.get_face_deltas());
	vector<point> nonasdDifference = subtractPointVectors(nonasdData.get_face_deltas(), inputData.get_face_deltas());

	vector<point> asdD_1;
	vector<point> asdD_2;
	vector<point> asdD_3;
	vector<point> asdD_4;
	vector<point> asdD_5;


	for (int i = 0; i < (asdDifference.size() / 5); i++){
		asdD_1.push_back(asdDifference[i]);
	}

	for (int i = (asdDifference.size() / 5); i < (2 * (asdDifference.size() / 5)); i++){
		asdD_2.push_back(asdDifference[i]);
	}

	for (int i = (2 * (asdDifference.size() / 5)); i < (3 * (asdDifference.size() / 5)); i++){
		asdD_3.push_back(asdDifference[i]);
	}

	for (int i = (3 * (asdDifference.size() / 5)); i < (4 * (asdDifference.size() / 5)); i++){
		asdD_4.push_back(asdDifference[i]);
	}

	for (int i = (4 * (asdDifference.size() / 5)); i < (5 * (asdDifference.size() / 5)); i++){
		asdD_5.push_back(asdDifference[i]);
	}

	int sumx = 0;
	int sumy = 0;

	for (int i = 0; i < asdD_1.size(); i++){
		sumx += asdD_1[i].x;
		sumy += asdD_1[i].y;
	}
	int aASD_1x = sumx / asdD_1.size();
	int aASD_1y = sumy / asdD_1.size();

	sumx = 0;
	sumy = 0;

	for (int i = 0; i < asdD_2.size(); i++){
		sumx += asdD_2[i].x;
		sumy += asdD_2[i].y;
	}
	int aASD_2x = sumx / asdD_2.size();
	int aASD_2y = sumy / asdD_2.size();

	sumx = 0;
	sumy = 0;

	for (int i = 0; i < asdD_3.size(); i++){
		sumx += asdD_3[i].x;
		sumy += asdD_3[i].y;
	}
	int aASD_3x = sumx / asdD_3.size();
	int aASD_3y = sumy / asdD_3.size();

	sumx = 0;
	sumy = 0;


	for (int i = 0; i < asdD_4.size(); i++){
		sumx += asdD_4[i].x;
		sumy += asdD_4[i].y;
	}
	int aASD_4x = sumx / asdD_4.size();
	int aASD_4y = sumy / asdD_4.size();

	sumx = 0;
	sumy = 0;


	for (int i = 0; i < asdD_5.size(); i++){
		sumx += asdD_5[i].x;
		sumy += asdD_5[i].y;
	}
	int aASD_5x = sumx / asdD_5.size();
	int aASD_5y = sumy / asdD_5.size();

	sumx = 0;
	sumy = 0;



	vector<point> nonasdD_1;
	vector<point> nonasdD_2;
	vector<point> nonasdD_3;
	vector<point> nonasdD_4;
	vector<point> nonasdD_5;

	for (int i = 0; i < (nonasdDifference.size() / 5); i++){
		nonasdD_1.push_back(nonasdDifference[i]);
	}

	for (int i = (nonasdDifference.size() / 5); i < (2 * (nonasdDifference.size() / 5)); i++){
		nonasdD_2.push_back(nonasdDifference[i]);
	}

	for (int i = (2 * (nonasdDifference.size() / 5)); i < (3 * (nonasdDifference.size() / 5)); i++){
		nonasdD_3.push_back(nonasdDifference[i]);
	}

	for (int i = (3 * (nonasdDifference.size() / 5)); i < (4 * (nonasdDifference.size() / 5)); i++){
		nonasdD_4.push_back(nonasdDifference[i]);
	}

	for (int i = (4 * (nonasdDifference.size() / 5)); i < (5 * (nonasdDifference.size() / 5)); i++){
		nonasdD_5.push_back(nonasdDifference[i]);
	}

	for (int i = 0; i < nonasdD_1.size(); i++){
		sumx += nonasdD_1[i].x;
		sumy += nonasdD_1[i].y;
	}
	int nonaASD_1x = sumx / nonasdD_1.size();
	int nonaASD_1y = sumy / nonasdD_1.size();

	sumx = 0;
	sumy = 0;

	for (int i = 0; i < nonasdD_2.size(); i++){
		sumx += nonasdD_2[i].x;
		sumy += nonasdD_2[i].y;
	}
	int nonaASD_2x = sumx / nonasdD_2.size();
	int nonaASD_2y = sumy / nonasdD_2.size();

	sumx = 0;
	sumy = 0;


	for (int i = 0; i < nonasdD_3.size(); i++){
		sumx += nonasdD_3[i].x;
		sumy += nonasdD_3[i].y;
	}
	int nonaASD_3x = sumx / nonasdD_3.size();
	int nonaASD_3y = sumy / nonasdD_3.size();

	sumx = 0;
	sumy = 0;


	for (int i = 0; i < nonasdD_4.size(); i++){
		sumx += nonasdD_4[i].x;
		sumy += nonasdD_4[i].y;
	}
	int nonaASD_4x = sumx / nonasdD_4.size();
	int nonaASD_4y = sumy / nonasdD_4.size();

	sumx = 0;
	sumy = 0;


	for (int i = 0; i < nonasdD_5.size(); i++){
		sumx += nonasdD_5[i].x;
		sumy += nonasdD_5[i].y;
	}
	int nonaASD_5x = sumx / nonasdD_5.size();
	int nonaASD_5y = sumy / nonasdD_5.size();

	sumx = 0;
	sumy = 0;




	int lASD = 0;
	int lnonASD = 0;

	if (aASD_1x <= nonaASD_1x){
		lASD++;
	}
	else
	{
		lnonASD++;
	}
	
	if (aASD_1y <= nonaASD_1y){
		lASD++;
	}
	else
	{
		lnonASD++;
	}

	if (aASD_2x <= nonaASD_2x){
		lASD++;
	}
	else
	{
		lnonASD++;
	}

	if (aASD_2y <= nonaASD_2y){
		lASD++;
	}
	else
	{
		lnonASD++;
	}
	
	if (aASD_3x <= nonaASD_3x){
		lASD++;
	}
	else
	{
		lnonASD++;
	}
	
	if (aASD_3y <= nonaASD_3y){
		lASD++;
	}
	else
	{
		lnonASD++;
	}

	if (aASD_4x <= nonaASD_4x){
		lASD++;
	}
	else
	{
		lnonASD++;
	}

	if (aASD_4y <= nonaASD_4y){
		lASD++;
	}
	else
	{
		lnonASD++;
	}


	if (aASD_5x <= nonaASD_5x){
		lASD++;
	}
	else
	{
		lnonASD++;
	}


	if (aASD_5y <= nonaASD_5y){
		lASD++;
	}
	else
	{
		lnonASD++;
	}


	cout << "ASD Count: " << lASD << endl;
	cout << "non ASD Count: " << lnonASD << endl;

	system("pause");
	return 0;
}

