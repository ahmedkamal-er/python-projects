def main():
    print("Welcome to Job Eligibility Portal")
    print("Please answer the following questions to check your eligibility for the job.")
    python =input("Do you know how to use  python ").lower().strip()
    experience=int(input("how many years of experience u got? "))
    qualified =input("do you have a degree in computer science? or partcipated in a bootcamp?  ").lower().strip()

    if python == "yes" and (experience >= 2 or qualified == "yes"):
        print("You are qualified  for the job")
    else:
        print("YOUR QUALIFICATION DOES NOT MEET THE REQUIREMENTS FOR THIS JOB")

if __name__ == "__main__":
    main()
