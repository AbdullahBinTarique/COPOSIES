//globals
var finalarr = [];
var countarr = [];
var unanswered = [];
var answered = [];
var attainment = [];
var attainmentlvl = [];
var internalweightarray = [];
var teethreshold = 60;





//for internal weighted average we need these variables
// let co1 = 0, co2 = 0, co3 = 0, co4 = 0, co5 = 0, co6 = 0;
// let countco1 = 0, countco2 = 0, countco3 = 0, countco4 = 0, countco5 = 0, countco6 = 0;
var CO = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
var countCO = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];

class formula {
    static thresholdpercinmarks(thresh, marks) {
        return thresh * marks / 100;
    }

    static countabovethreshold(column, marks) {
        let count = 0;
        for (let x = 0; x < marks.length; x++) {
            if (marks[x] >= finalarr[column - 1]) {  //columns are basically question numbers
                count++;
            }
        }
        return count;
    }
    //Third function excell csc 304 row 173
    static obtaineddivbyTstudents(noofquestions) {
        for (let x = 0; x < noofquestions; x++) {
            attainment[x] = countarr[x] * 100 / answered[x];
        }
        console.log(attainment);
    }
    // fourth function excell csc 304 row 174
    static lvlattainment(lvl1, lvl2, lvl3) {
        const attainmentperc = [...attainment];
        let y = 0;
        for (let x in attainmentperc) {
            // switch(parseInt(attainmentperc[x])){
            //     case parseInt(attainmentperc[x])>= lvl3: attainmentlvl[y] = 3; y++; break;
            //     case parseInt(attainmentperc[x])>= lvl2: attainmentlvl[y] = 2; y++; break;
            //     case parseInt(attainmentperc[x])>= lvl1: attainmentlvl[y] = 1; y++; break;
            //     default :attainmentlvl[y] = 0; y++;
            //     }    
            // }

            if (attainmentperc[x] >= lvl3) {
                attainmentlvl[y] = 3; y++;

            }
            else if (attainmentperc[x] >= lvl2) { attainmentlvl[y] = 2; y++; }
            else if (attainmentperc[x] >= lvl1) { attainmentlvl[y] = 1; y++; }
            else { attainmentlvl[y] = 0; y++; }
        }
    }



}
var thresh = 60;//value from the backend

class calc {

    //to be called first excell csc 304 row 171
    static thresholdcalcforquestions(noofquestions, Marksia) {  //no of question will come from the backend
        let arr = [];
        let b = 0;
        for (let x = 1; x <= noofquestions; x++) {
            b = document.getElementById(Marksia + x).value;
            arr.push(b);
        }
        for (let x = 1; x <= noofquestions; x++)
            finalarr.push(formula.thresholdpercinmarks(thresh, arr[x - 1]));
        //   console.log(finalarr);
    }

    //second function excell csc 304 row 172
    static thresholdpercandabove(noofquestions, QA) {
        let arr = [];

        for (let y = 1; y <= noofquestions; y++) {
            let fields = document.getElementsByName(QA + y);
            // answered[y-1] = fields.length;
            for (let x = 0, z = 0; x < fields.length; x++) {
                if (fields[x].value.trim() == "") {

                }
                else {
                    arr[z] = (fields[x].value);
                    z++;
                }
            }
            countarr.push(formula.countabovethreshold(y, arr));
            answered[y - 1] = arr.length;
            unanswered[y - 1] = fields.length - arr.length   //excell csc 304 row 175
            arr = [];
        }
        console.log(arr);
    }
    //5th function excell csc 304 I 185
    static weighted_avg_of_internal(noofquestions, COia) {



        let arr = [];
        for (let b = 0; b < noofquestions; b++) {
            let c = (document.getElementById(COia + (b + 1)).value);
            arr.push(c)
        }
        let x = 0;
        for (let i = 0; i < cos; i++) {
            if (CO[i] == NaN) {
                CO[i] = 0;
                countCO[i] = 0;
            }
        }
        for (let b in arr) {
            for (let i = 0; i < cos; i++) {
                if (arr[b] == i + 1) {
                    CO[i] += attainmentlvl[x]

                    countCO[i]++;
                }
            }

            // {if (arr[b] == 1) {
            //     co1 += attainmentlvl[x]

            //     countco1++;
            // }
            // else if (arr[b] == 2) {

            //     co2 += attainmentlvl[x]

            //     countco2++;

            // }
            // else if (arr[b] == 3) {

            //     co3 += attainmentlvl[x]

            //     countco3++;

            // }
            // else if (arr[b] == 4) {

            //     co4 += attainmentlvl[x]

            //     countco4++;

            // } else if (arr[b] == 5) {

            //     co5 += attainmentlvl[x]

            //     countco5++;

            // } else if (arr[b] == 6) {

            //     co6 += attainmentlvl[x]

            //     countco6++;

            // }}
            x++;
        }
        let b = 0;
        for (let i = 0; i < cos; i++) {
            internalweightarray[b++] = CO[i] / countCO[i];
        }
        // internalweightarray[b++] = co1 / countco1;
        // internalweightarray[b++] = co2 / countco2;
        // internalweightarray[b++] = co3 / countco3;
        // internalweightarray[b++] = co4 / countco4;
        // internalweightarray[b++] = co5 / countco5;
        // internalweightarray[b++] = co6 / countco6;

        for (let x = 1; x <= cos; x++) {

            for (let i = 0; i < cos; i++) {
                if (x == i + 1 && internalweightarray[x - 1] != NaN) {
                    document.getElementById('Co' + (i + 1) + 'I').innerHTML = internalweightarray[x - 1];
                }
            }

            // if (x == 1 && internalweightarray[x - 1] != NaN) {
            //     document.getElementById('Co1I').innerHTML = internalweightarray[x - 1];
            // }
            // else if (x == 2 && internalweightarray[x - 1] != NaN) {
            //     document.getElementById('Co2I').innerHTML = internalweightarray[x - 1];
            // }
            // else if (x == 3 && internalweightarray[x - 1] != NaN) {
            //     document.getElementById('Co3I').innerHTML = internalweightarray[x - 1];
            // } else if (x == 4 && internalweightarray[x - 1] != NaN) {
            //     document.getElementById('Co4I').innerHTML = internalweightarray[x - 1];
            // } else if (x == 5 && internalweightarray[x - 1] != NaN) {
            //     document.getElementById('Co5I').innerHTML = internalweightarray[x - 1];
            // } else if (x == 6 && internalweightarray[x - 1] != NaN) {
            //     document.getElementById('Co6I').innerHTML = internalweightarray[x - 1];
            // }
        }


    }
    //6th function for csc 304 J185
    static weighted_avg_of_external(lvl1, lvl2, lvl3) {
        let arr = []
        let narr = [...document.getElementsByName('TEE')];
        for (let x in narr) {
            arr[x] = narr[x].value;
        }
        let b = document.getElementById('MARKSTEE').value
        finalarr[finalarr.length] = formula.thresholdpercinmarks(teethreshold, b);
        let cl = 0;
        cl = countarr.length;
        countarr.push(formula.countabovethreshold(cl + 1, arr));
        attainment[attainment.length] = countarr[cl] * 100 / arr.length;
        attainmentlvl[attainmentlvl.length] = (attainment[attainment.length - 1] >= lvl3) ? 3 : (attainment[attainment.length - 1] >= lvl2) ? 2 : (attainment[attainment.length - 1] >= lvl1) ? 1 : 0;

        // if(attainment[attainment.length-1] >= lvl3)
        //     attainmentlvl[attainment.length] = 3
        // else if(attainment[attainment.length-1] >= lvl2) 
        //     attainmentlvl[attainment.length] = 2
        // else if(attainment[attainment.length-1] >= lvl1) 
        //     attainmentlvl[attainment.length] = 1
        // else
        // attainmentlvl[attainment.length] = 0
    }



    static print(noofquestion, ThreshMarksIA, Coatia, AttlvlIA) {
        let Thresharr = [];
        for (let x = 0; x < noofquestion; x++) {
            document.getElementById(ThreshMarksIA + (x + 1)).innerHTML = finalarr[x];
            document.getElementById(Coatia + (x + 1)).innerHTML = countarr[x];

            document.getElementById(AttlvlIA + (x + 1)).innerHTML = Math.round(attainment[x] * 10) / 10;

        }
        document.getElementById('ThreshMarksTEE').innerHTML = finalarr[finalarr.length - 1];
        document.getElementById('CountTEE').innerHTML = countarr[countarr.length - 1];

        document.getElementById('MARKSTEE').innerHTML = Math.round(attainment[attainment.length - 1] * 10) / 10;
    }




    static TweightedAvgAchieved() {

        for (let x = 0; x < cos; x++) {
            let b = [], c = [];
            b = [...document.getElementsByName('Co' + (x + 1))]
            for (let y = 0; y < b.length; y++) {
                c.push(b[y].value);
            }
            coposcore.push(c);

        }
        // return coposcore;
    }

    static CaclextWeightedAvg() {
        let b = 0;
        for (let x = 0; x < cos; x++) {
            b = document.getElementById('Co' + (x + 1) + 'I').textContent;

            // document.getElementById("Co"+(x+1) +"I").innerHTML = 1211;

            extWeightedAvg[x] = Math.round(((0.2 * b) + (0.8 * attainmentlvl[attainmentlvl.length - 1])) * 10) / 10;
        }
        let arr = [];
        arr = [...document.getElementsByName("External")];
        for (let a = 0; a < arr.length; a++) {
            document.getElementById("Co" + (a + 1) + "E").innerHTML = extWeightedAvg[a];
            // document.getElementById("Co" + (a + 1) + "E").innerHTML = 1211;

        }

    }

    static calAvgOfRel() {
        for (let index = 0; index < (parseInt(pos) + parseInt(psos)); index++) {
            let arr = [];
            for (let a = 0; a < cos; a++) {
                if (index < pos) {
                    let ele = document.getElementById(`posAchieved${index + 1}-Co${a + 1}`).textContent;
                    arr.push(ele);
                }
                else {
                    let ele = document.getElementById(`psosAchieved${index + 1 - pos}-Co${a + 1}`).textContent;
                    arr.push(ele);

                }

            } let avg = 0.0, sum = 0.0, count = 0;

            for (let b = 0; b < arr.length; b++) {
                if (arr[b] != "" && arr[b] != "NaN") {
                    sum += parseFloat(arr[b]);
                    count++;
                }
            }
            avg = Math.round(sum / count * 100) / 100;
            storeelements.push(avg);
        }
        for (let index = 0; index < storeelements.length; index++) {
            if (index < pos) {
                document.getElementById(`posAvg${(index + 1)}`).innerHTML = storeelements[index];

            }
            else {
                document.getElementById(`psosAvg${(index + 1 - pos)}`).innerHTML = storeelements[index];

            }
        }
        storeelements = [];

    }



    static calcWeightedAvgAchieved() {
        let variable = parseInt(psos) + parseInt(pos);
        for (let i = 0; i < coposcore.length; i++) {
            for (let j = 0; j < variable; j++) {
                let k = coposcore[i][j];
                if (k === '3' && j < pos) {
                    document.getElementById(`posAchieved${j + 1}-Co${i + 1}`).innerHTML = Math.round(extWeightedAvg[i] * 10) / 10;
                }
                else if (k === '2' && j < pos) {
                    document.getElementById(`posAchieved${j + 1}-Co${i + 1}`).innerHTML = Math.round(extWeightedAvg[i] * 0.6 * 10) / 10;
                }
                else if (k === '1' && j < pos) {
                    document.getElementById(`posAchieved${j + 1}-Co${i + 1}`).innerHTML = Math.round(extWeightedAvg[i] * 10 * 0.33) / 10;
                }
                else if (k === '0' && j < pos) {
                    document.getElementById(`posAchieved${j + 1}-Co${i + 1}`).innerHTML = 0;

                }
                ///////////////////////////
                else if (k === '3' && j >= pos) {
                    document.getElementById(`psosAchieved${j + 1 - pos}-Co${i + 1}`).innerHTML = Math.round(extWeightedAvg[i] * 10) / 10;
                }
                else if (k === '2' && j >= pos) {
                    document.getElementById(`psosAchieved${j + 1 - pos}-Co${i + 1}`).innerHTML = Math.round(extWeightedAvg[i] * 0.6 * 10) / 10;
                }
                else if (k === '1' && j >= pos) {
                    document.getElementById(`psosAchieved${j + 1 - pos}-Co${i + 1}`).innerHTML = Math.round(extWeightedAvg[i] * 10 * 0.33) / 10;
                }
                else if (k === '0' && j >= pos) {
                    document.getElementById(`psosAchieved${j + 1 - pos}-Co${i + 1}`).innerHTML = 0;

                }/////////////////////////
                else if (j < pos) {
                    document.getElementById(`posAchieved${j + 1}-Co${i + 1}`).innerHTML = '';
                }
                else if (j >= pos) {
                    document.getElementById(`psosAchieved${j + 1 - pos}-Co${i + 1}`).innerHTML = '';
                }

            }
        }
        this.calAvgOfRel()
    }


    static Ethersholdcalc() {

        for (let i = 0; i < cos; i++) {
            let ele = document.getElementsByName('ECoAchieved' + (i + 1))
            for (let j = 0; j < (parseInt(pos) + parseInt(psos)); j++) {
                if (coposcore[i][j] != "" && coposcore[i][j] != "NaN") {
                    ele[j].innerHTML = extWeightedAvg[i];
                }

            }
        }
        ///for calculating the average
        for (let index = 0; index < (parseInt(pos) + parseInt(psos)); index++) {
            let arr = [];
            for (let a = 0; a < cos; a++) {
                if (index < pos) {
                    let ele = document.getElementById(`EposAchieved${index + 1}-Co${a + 1}`).textContent;
                    arr.push(ele);
                }
                else {
                    let ele = document.getElementById(`EpsosAchieved${index + 1 - pos}-Co${a + 1}`).textContent;
                    arr.push(ele);

                }

            } let avg = 0.0, sum = 0.0, count = 0;

            for (let b = 0; b < arr.length; b++) {
                if (arr[b] != " " && arr[b] != "NaN") {
                    sum += parseFloat(arr[b]);
                    count++;
                }
            }
            avg = Math.round(sum / count * 100) / 100;
            storeelements.push(avg);
        }
        for (let index = 0; index < storeelements.length; index++) {
            if (index < pos) {
                document.getElementById(`EposAvg${(index + 1)}`).innerHTML = storeelements[index];

            }
            else {
                document.getElementById(`EpsosAvg${(index + 1 - pos)}`).innerHTML = storeelements[index];

            }
        }
        let max = 0;
        for (let a = 0; a < parseInt(cos); a++) {
            let nodelist = document.getElementsByName('Co' + (a + 1));

            for (let e of nodelist) {
                if (e.value > max) {
                    max = e.value
                }
            }
        }
        let nodelist = document.getElementsByName('TargetSet');
        for (let a of nodelist) {
            a.innerHTML = max;
        }


    }

    static TargetNAvg() {
        let max = 0;
        for (let a = 0; a < parseInt(cos); a++) {
            let nodelist = document.getElementsByName('Co' + (a + 1));

            for (let e of nodelist) {
                if (e.value > max) {
                    max = e.value
                }
            }
        }
        let nodelist = document.getElementsByName('Targetdata');
        for (let a of nodelist) {
            a.innerHTML = max;
        }
        ///Averaging the Target Set
        let top = 0;
        let value = document.getElementsByName('Targetavg');
        for (let index = 0; index < (parseInt(pos) + parseInt(psos)); index++) {
            let arr = [];
            for (let a = 0; a < cos; a++) {
                if (index < pos) {
                    let ele = document.getElementById(`pos${index + 1}-Co${a + 1}`).value;
                    arr.push(ele);
                }
                else {
                    let ele = document.getElementById(`psos${index + 1 - pos}-Co${a + 1}`).value;
                    arr.push(ele);

                }

            } let avg = 0.0, sum = 0.0, count = 0;
            for (let b = 0; b < arr.length; b++) {
                if (arr[b] != "" && arr[b] != "NaN") {
                    sum += parseFloat(arr[b]);
                    count++;
                }
            }
            avg = Math.round(sum / count * 100) / 100;
            value[top].innerHTML = (avg);
            top++;
        }

    }

    static targetAchieved() {
        let checkvalue = 90;
        let top = 0;
        let avglist = document.getElementsByName('EAVG');
        let list = document.getElementsByName('Achieved')
        for (let a of list) {
            if (((Math.round(((avglist[top].textContent) / 3) * 100) * 10) / 10) >= checkvalue) {
                a.innerHTML = "Y"
            }
            else {
                a.innerHTML = "N"
            }
            top++;
        }
    }


}
var coposcore = [];
var extWeightedAvg = [];//2D array
var storeelements = [];//1D array

class mainFunctions {
    static calculate1(noofquestion, lv1, lvl2, lvl3) {
        calc.thresholdcalcforquestions(noofquestion, "MARKSia1");
        calc.thresholdpercandabove(noofquestion, "QA");
        formula.obtaineddivbyTstudents(noofquestion);
        formula.lvlattainment(lv1, lvl2, lvl3);
        calc.weighted_avg_of_internal(noofquestion, "COia1");

        calc.print(noofquestion, "ThreshMarksIA1", "Coatia1", "AttlvlIA1");
        finalarr = [];
        countarr = [];
        unanswered = [];
        answered = [];
        attainment = [];
        attainmentlvl = [];
        // internalweightarray = [];
        teethreshold = 60;
    }

    static calculate2(noofquestion, lv1, lvl2, lvl3) {
        calc.thresholdcalcforquestions(noofquestion, "MARKSia2");
        calc.thresholdpercandabove(noofquestion, "QA1");
        formula.obtaineddivbyTstudents(noofquestion);
        formula.lvlattainment(lv1, lvl2, lvl3);
        calc.weighted_avg_of_internal(noofquestion, "COia2");
        calc.weighted_avg_of_external(lv1, lvl2, lvl3);
        calc.print(noofquestion, "ThreshMarksIA2", "Coatia2", "AttlvlIA2");

    }


    static calculateAchievedAndExternal() {

        calc.CaclextWeightedAvg();
        calc.calcWeightedAvgAchieved();
        calc.Ethersholdcalc();
        calc.targetAchieved();




    }

}