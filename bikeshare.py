import time

import pandas as pd

import numpy as np

from scipy import stats



CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }



def get_filters():
    
	"""
	Asks user to specify a city, month, and day to analyze.

    
	Returns:
        
	(str) city - name of the city to analyze
        
	(str) month - name of the month to filter by, or "all" to apply no month filter
        
	(str) day - name of the day of week to filter by, or "all" to apply no day filter
    
	"""
	print('Hello! Let\'s explore some US bikeshare data!')
	while True:
        
		try: 
            
			city=input("\nEnter the name of the city You would like to view.\n You have 3 options:\n chicago,\n new york city,\n washingtion. \n Please enter the choice exactly as seen here.\n Remember, you only have these options,\n and we do not have gender and year of birth entries in washington(Sorry about that)\n\n")
			city=city.lower()
            
			if(city=='chicago' or city=='new york city' or city =='washington'):
				break
            
			else:
               
				print('-'*40,"\n That is not among the options, or you havent entered it correctly. Please try again \n",'-'*40)
				continue       
		except :             
			print("\n Oops! There was an error in the input. Please try again.\n")			    	
	print("\n Okay, you chose ",city,".\n")     
	while True:       
		try:            
			month=input("Now, lets set our filter for month of the year.\n You can view only the first 6 months.\n Enter the name of the month you would like to view in small letters(ex. january, february),\n or remove the month filter by entering 'all' \n")            
			month=month.lower()           
			if( month== 'january' or month == 'february' or month =='march' or month =='april' or month == 'may' or month =='june' or month=='all'):
				break
			else:    
				print('-'*40,"\nSorry, thats not a valid input. Please try again.\n",'-'*40)
				continue       
		except:           
			print(" Oops! there is an error with your input. Please try again") 
	if (month!='all'):          
		print("\n So, we're looking at the month ",month,"\n")  
	else:        
		print("No filter it is.")   
# get user input for month (all, january, february, ... , june)  
	while True:
		try:            
			day=input("Now, lets set our filter for the day of the week.\n Enter the day of the week you would like to view in small letters(ex: monday, tuesday), \n or remove this filter by entering 'all' \n")            
			day=day.lower()            
			if (day=='monday' or day=='tuesday' or day=='wednesday' or day=='thursday' or day=='friday' or day=='saturday' or day=='sunday' or day=='all'):
				break            
			else:                
				print('-'*40,"\nSorry, thats not a valid input. Please try again.\n",'-'*40)                
				continue        
		except:            
			print(" Oops! there is an error with your input. Please try again")    
		if (day!='all'):        
			print("\n So, we're looking at the day ",day,"\n")    
		else:       
			print("No filter it is.") 
# get user input for day of week (all, monday, tuesday, ... sunday)
	print('-'*40)
	return city, month, day
def load_data(city, month, day):
	"""
Loads data for the specified city and filters by month and day if applicable.	
Args:       
(str) city - name of the city to analyze        
(str) month - name of the month to filter by, or "all" to apply no month filter
(str) day - name of the day of week to filter by, or "all" to apply no day filter    
	Returns:        
df - Pandas DataFrame containing city data filtered by month and day"""   
	df = pd.read_csv(CITY_DATA[city])    
	df['Start Time'] = pd.to_datetime(df['Start Time'])    
	df['months'] = df['Start Time'].dt.month    
	df['weekday'] = df['Start Time'].dt.day_name       
	if(month != 'all'):        
		months = ['january','february','march','april','may','june']        
		month = months.index(month)+1        
		df = df[df['months'] == month]    
		if (day != 'all'):        
			df=df[df['weekday'] == day.title()]    
	return df
def time_stats(df):
    
	
	"""Displays statistics on the most frequent times of travel."""   
	print('\nCalculating The Most Frequent Times of Travel...\n')    
	start_time = time.time()    
	print("\n The most common month is: ",df['months'].mode()[0],"\n")
# display the most common month    
	print("\nThe most common day of the week is: ",df['weekday'].mode()[0],"\n")
# display the most common day of week    
	print("\nThe most common start hour is: ",df['Start Time'].dt.hour.mode()[0],"\n")
# display the most common start hour    
	print("\nThis took %s seconds." % (time.time() - start_time))    
	print('-'*40) 
def station_stats(df):
	"""Displays statistics on the most popular stations and trip."""
	print('\nCalculating The Most Popular Stations and Trip...\n')
	start_time = time.time()
	print("\n The most common start station is: ",df['Start Station'].mode()[0],"\n")
# display most commonly used start station    
	print("\n The most common end station is: ",df['End Station'].mode()[0],"\n")
# display most commonly used end station
	group1= df['Start Station'].values
	group2= df['End Station'].values
	group3=group1+","+ group2
	group3=pd.DataFrame(group3)
	print("The most popular trip is in between the stations: ",group3.mode()[0][0])
# display most frequent combination of start station and end station trip   
	print("\nThis took %s seconds." % (time.time() - start_time))
	print('-'*40)
def trip_duration_stats(df,):    
	"""Displays statistics on the total and average trip duration."""
	print('\nCalculating Trip Duration...\n')
	start_time = time.time()
	df['End Time']=pd.to_datetime(df['End Time'])
	df['Travel Time']=df['End Time'].sub(df['Start Time'])
	print("Total travel time: ",df['Travel Time'].sum())
# display total travel time    
	print("Mean travel time: ",df['Travel Time'].mean())
# TO DO: display mean travel time    
	print("\nThis took %s seconds." % (time.time() - start_time))
	print('-'*40)
def user_stats(df,city):    
	"""Displays statistics on bikeshare users."""
	print('\nCalculating User Stats...\n')   
	start_time = time.time()    
	print("\nThe types of users, with their count, are shown below: \n")   
	print (df['User Type'].value_counts(),"\n")
# Display counts of user types    
	if city != 'washington':        
		print (df['Gender'].value_counts(),"\n")
# Display counts of gender        
		print("Earliest year of birth: ",df['Birth Year'].min())       
		print("Most recent year of birth: ",df['Birth Year'].max())        
		print("Most common year of birth: ",df['Birth Year'].mode()[0]) 
# Display earliest, most recent, and most common year of birth          
	print("\nThis took %s seconds." % (time.time() - start_time))   
	print('-'*40)
def display_data(df):       
	lim1=0       
	lim2=5        
	while True:           
		choice=input("\nDo you want to see the raw data? [yes/no]\n")            
		choice=choice.lower()            
		if choice=='yes':               
			while True:                    
				for i in range(lim1,lim2):                        
					print(df.iloc[i],"_"*50)                   
				choice=input("\nWould you like to view more? [yes/no]\n ")                    
				if choice.lower()=='yes':                        
					lim1+=5                        
					lim2+=5                    
				elif choice.lower()=='no':                       
					lim2=0       
					break                    
				else:
					print("Sorry, didnt get you. Please try again.")            
		elif choice=='no':                
			lim2=0	 
	#condition for exiting the bigger while loop            
		else:
			print("\nSorry, didnt get you. Please try again\n")            
		if lim2==0:                
			break        
def main():    
	while True:        
		city, month, day = get_filters()        
		df = load_data(city, month, day)        
		#time_stats(df)        
		station_stats(df)        
		trip_duration_stats(df)        
		user_stats(df,city)        
		display_data(df)        
		restart = input('\nWould you like to restart? Enter yes or no.\n')        
		if restart.lower() != 'yes':            
			break
if __name__ == "__main__":
	main()
