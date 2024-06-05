This proram performs Advanced Boolean Algebra like Shannon Co-factoring, Boolean Difference, Consensus, Smoothing function on a given SOP for the entered splitting variable. 

The program contains two parts - Finding the Shannon cofactors and the finding the rest. 

Common input for both parts is the SOP function.

Shannon Co-factoring:

    To find the co-factor, a variable or a cube can be entered as input. For example sample output:
        "This program is to generate shanon co-factors of a given Boolean function.				
        Boolean function is given as a CSV file with rows as cubes and coloumns as literals.				
        For uncomplemented literal, represent using lower case and for complemented literal, represent using upper case.				
        Enter the function: abc+Abc+aBc+abC				
        Enter splitting variable/cube: AB				
        f_AB = 0"			
				
	Another example:
        "This program is to generate shanon co-factors of a given Boolean function.				
        Boolean function is given as a CSV file with rows as cubes and coloumns as literals.				
        For uncomplemented literal, represent using lower case and for complemented literal, represent using upper case.				
        Enter the function: ab+Bcd+bD+ABD+ad				
        Enter splitting variable/cube: D				
        f_D = ab+b+AB"

Other functions:

    After finding co-factors, it asks again for the splitting variable. Now only one variable needs to be entered. For example:		
        "Continue with finding Boolean difference, Consensus and Smoothing function. Enter the splitting variable: b
        Boolean difference of the function with respect to b is: (ac+Ac+aC)^(ac)				
        Consensus of the function with respect to b is: ac				
        Smoothing function of the function with respect to b is: ac+Ac+aC"    
				
	Another example:    
		"Continue with finding Boolean difference, Consensus and Smoothing function. Enter the splitting variable: D       
		Boolean difference of the function with respect to D is: (ab+b+AB)^(ab+Bc+a)
		Consensus of the function with respect to D is: ba+BcA        
		Smoothing function of the function with respect to D is: ab+b+AB+Bc+a"

Further, the functions can be modified to simplify the final results using basic boolean algebra. The XOR function can be expanded and further simplified. 
