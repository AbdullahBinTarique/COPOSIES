//globals
var finalarr = [];
var countarr = [];
var unanswered = [];
var answered = [] ;
var attainment = [];
var attainmentlvl = [];
var internalweightarray = [];
var teethreshold = 60 ;


class formula{
    static thresholdpercinmarks(thresh,marks){
        return thresh*marks/100;
    }

    static countabovethreshold(column,marks){
        let count = 0;
        for(let x=0 ; x < marks.length ; x++){
            if ( marks[x]>=finalarr[column-1] ){  //columns are basically question numbers
                count++;
            }
            }
        return count;
     }
     //Third function excell csc 304 row 173
    static obtaineddivbyTstudents(noofquestions ){
        for(let x = 0;x < noofquestions; x++ ){
            attainment[x] = countarr[x]*100/answered[x] ;
        }
        console.log(attainment);
    }
    // fourth function excell csc 304 row 174
    static lvlattainment(lvl1, lvl2, lvl3){
        const attainmentperc = [...attainment];
        let y=0;
        for (let x in attainmentperc){
        // switch(parseInt(attainmentperc[x])){
        //     case parseInt(attainmentperc[x])>= lvl3: attainmentlvl[y] = 3; y++; break;
        //     case parseInt(attainmentperc[x])>= lvl2: attainmentlvl[y] = 2; y++; break;
        //     case parseInt(attainmentperc[x])>= lvl1: attainmentlvl[y] = 1; y++; break;
        //     default :attainmentlvl[y] = 0; y++;
        //     }    
        // }

        if(attainmentperc[x]>=lvl3)
        {attainmentlvl[y] = 3; y++;

        }
        else if(attainmentperc[x]>=lvl2)
        { attainmentlvl[y] = 2; y++;}
        else if (attainmentperc[x]>=lvl1)
        { attainmentlvl[y] = 1; y++;}
        else{attainmentlvl[y] = 0; y++;}
    }
    }
    


}
var thresh = 60;//value from the backend

class calc{

    //to be called first excell csc 304 row 171
    static thresholdcalcforquestions( noofquestions){  //no of question will come from the backend
        let arr = [];
        let b = 0;
        for(let x = 1;x <= noofquestions; x++){
            b = document.getElementById('MARKSia1'+x).value;
            arr.push(b);
        }
        for(let x=1 ;x <= noofquestions; x++)
            finalarr.push(formula.thresholdpercinmarks(thresh,arr[x-1]));
    //   console.log(finalarr);
    }

    //second function excell csc 304 row 172
    static thresholdpercandabove(noofquestions ){
         let arr = []; 
        
        for(let y = 1 ; y <= noofquestions ; y++){
            let fields = document.getElementsByName('QA'+y );
            // answered[y-1] = fields.length;
            for(let x = 0,z=0 ; x<fields.length ;x++ ){
            if(fields[x].value.trim() == ""){
             
            }
            else{
                arr[z] = (fields[x].value)   ;  
                z++;
            }
            }
            countarr.push(formula.countabovethreshold(y,arr));
            answered[y-1] =  arr.length; 
            unanswered[y-1] = fields.length - arr.length   //excell csc 304 row 175
            arr = [];
        }
        console.log(arr);
    }
    //5th function excell csc 304 I 185
    static weighted_avg_of_internal(noofquestions){

        let co1 = 0,co2 = 0,co3 = 0,co4 = 0,co5 = 0, co6 = 0;
        let countco1 = 0,countco2 = 0,countco3 = 0,countco4 = 0,countco5 = 0, countco6 = 0;

        let arr = [];
        for(let b=0;b<noofquestions;b++){
        let c = (document.getElementById('COia1' + (b+1)).value);
        arr.push(c)
        }
        let x = 0;
        for(let b in arr){
            if (arr[b] == 1){
                co1 += attainmentlvl[x]
                
                countco1++;
            }
            else if(arr[b] == 2){
                
                    co2 += attainmentlvl[x]
                    
                    countco2++;
                
            }
            else if(arr[b] == 3){
                
                    co3 += attainmentlvl[x]
                    
                    countco3++;
                
            }
            else if(arr[b] == 4){
                
                    co4 += attainmentlvl[x]
                    
                    countco4++;
                
            }else if(arr[b] == 5){
                
                    co5 += attainmentlvl[x]
                    
                    countco5++;
                
            }else if(arr[b] == 6){
                
                    co6 += attainmentlvl[x]
                    
                    countco6++;
                
            }
            x++;
        }
        let b = 0;
        internalweightarray[b++] = co1/countco1;
        internalweightarray[b++] = co2/countco2;
        internalweightarray[b++] = co3/countco3;
        internalweightarray[b++] = co4/countco4;
        internalweightarray[b++] = co5/countco5;
        internalweightarray[b++] = co6/countco6;
            
            
    }
    //6th function for csc 304 J185
    static weighted_avg_of_external(lvl1,lvl2,lvl3){
        let arr = []
        let narr = [...document.getElementsByName('TEE')];
        for(let x in narr){
            arr[x] = narr[x].value;
        }
        let b = document.getElementById('MARKSTEE').value
        finalarr[finalarr.length] = formula.thresholdpercinmarks(teethreshold,b);
        let cl = 0;
          cl = countarr.length;
            countarr.push(formula.countabovethreshold(cl +1 , arr));
            attainment[attainment.length] = countarr[cl]*100/arr.length ;    
            attainmentlvl[attainmentlvl.length] = (attainment[attainment.length-1]>=lvl3) ? 3 : (attainment[attainment.length-1]>=lvl2) ? 2 : (attainment[attainment.length-1]>=lvl1) ? 1: 0  ;

            // if(attainment[attainment.length-1] >= lvl3)
            //     attainmentlvl[attainment.length] = 3
            // else if(attainment[attainment.length-1] >= lvl2) 
            //     attainmentlvl[attainment.length] = 2
            // else if(attainment[attainment.length-1] >= lvl1) 
            //     attainmentlvl[attainment.length] = 1
            // else
            // attainmentlvl[attainment.length] = 0
    }

}
