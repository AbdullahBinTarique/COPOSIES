import pandas as pd
class Formulae:
    # calculates threshold_marks_percent per question (or sem paper)
    def formula1(threshold_marks_percent, marks):
        return (threshold_marks_percent * marks)//100

    # calculates count of students scoring threshold_marks_percent and above for a particular question (or sem paper)
    def formula2(threshold_marks_percent, marks_column):
        count = 0
        for marks in marks_column:
            if pd.notna(marks) and marks > formula1(threshold_marks_percent, marks):
                count += 1
        return count

    # Attainment Level in percent which calculates ratio of students scoring above threshold_marks_percent to the number of students who attempted that question as a percentage
    def formula3(threshold_marks_percent, marks_column, total_students):
        att_lvl_as_percent = (round(formula2(threshold_marks_percent, marks_column)/(total_students - formula5(marks_column))) * 100,2) if marks_column.sum() != 0 else  None
        return att_lvl_as_percent

    # Calculates Attainment Level based on pre-defined threshold settings for student count percent needed for a level
    def formula4(threshold_for_level1,threshold_for_level2,threshold_for_level3,threshold_marks_percent, marks_column, total_students):
        att_lvl_as_percent = formula3(threshold_marks_percent, marks_column, total_students)
        if att_lvl_as_percent >= threshold_for_level3:
            return 3
        elif att_lvl_as_percent >= threshold_for_level2:
            return 2
        elif att_lvl_as_percent >= threshold_for_level1:
            return 1
        else:
            return 0
        
    # counts number of students who did not attempt a specific sub-question
    def formula5(marks_column):
        return pd.isna(marks_column).sum()
    
    # Calculates Target Set for CO-PO Correlation Table which is the average for the values in a column of a specific PO but differing COs
    def formula6(PO_column):
        if PO_column.sum() == 0:
            return None
        else:
            return PO_column.mean()
        
    # Calculates Scaled Target Set which assigns Null value if Target Set is Null else return 3
    def formula7(target_set):
        for value in target_set:
            if pd.isna(value):
                return None
            else:
                return 3
            
    # Internal Weighted Average: this function returns None if Summation of values for a specific CO for all POs is 0, otherwise, it shall check wherever value of CO-PO mapping is 1 and add the corresponding value in Attainment table. It then divides the sum with the number of unit values in CO-PO mapping
    def formula8(CO_row,CO_mapped,att_lvl_row):
        if CO_row.sum() == 0:
            return None
        else:
            try:
                sum = 0
                for CO in CO_row:
                    if CO == CO_mapped:
                        sum += att_lvl_row[CO_mapped.index(CO)]/CO_row.count(1)
            except ZeroDivisionError:
                return 0
            return round(sum,1)

    # External Weighted Average: this function will return none if summation of a CO for all PO is 0 else it shall output (.2 * weighted average for internal i.e formula8 + .8 * Attainment level for TEE)
    def formula9(CO_row,CO_mapped,att_lvl_row):
        if CO_row.sum() == 0:
            return None
        else:
            return round((0.2*formula8(CO_row,CO_mapped,att_lvl_row))+(0.8*att_lvl_row[len(att_lvl_row-1)]),1)            
        
    # This function will return external weighted average if CO-PO correlation score is 3, 0.67 * external weighted average if correlation score is 2, 0.33 * external weighted average if correlation score is 1 else None
    def formula10(CO_PO_Correlation_score, external_weighted_average):
        if CO_PO_Correlation_score == 3:
            return External_weighted_average
        elif CO_PO_Correlation_score == 2:
            return External_weighted_average * 0.67
        elif CO_PO_Correlation_score == 1:
            return External_weighted_average * 0.33
        else:
            return None
        
    # Weighted Average Achieved: It shall return the value of average of column in CO-PO correlation Table 2 if the sum of values in the column are greater than 0 else it will return None
    def formula11(PO_column):
        if PO_column.sum() == 0:
            return None
        else:
            return PO_column.mean()

    # This function populates CO-PO table value with external weighted average
    def formula12(external_weighted_average,CO_PO_input):
        if CO_PO_input == 1 or CO_PO_input == 2 or CO_PO_input == 3:
            return external_weighted_average
        else:
            return None
        
    # Target Set (Average of Correlation) This shall populate data to Scaled target data if it is not Null else return None
    def formula13(scaled_target_value):
        if pd.isna(scaled_target_value):
            return None
        else:
            return scaled_target_value
        
    # Percent : This calculates the percentage of threshold based/ Scaled average by target set
    def formula14(scaled_average, target_set):
        if pd.isna(scaled_average):
            return None
        else:
            return round((scaled_average/target_set )* 100,2) 
        
    # For Course Exit Survey, it prints average of CO between 1 t0 3
    def formula15(CO_PO_entry,avg_CO_PO):
        if CO_PO_entry == 3 :
            return avg_CO_PO
        elif CO_PO_entry == 2:
            return avg_CO_PO * .67
        elif CO_PO_entry == 1:
            return avg_CO_PO * .33
        else:
            return None
            
            