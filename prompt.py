from terminaltables import AsciiTable
from sys import exit


class Todo(object):
    def __init__(self):
        self.skills_dict = {}

    def welcome(self):
        inp = input('''Welcome.
      You can do the following:
            1. Add skill
            2. View all skills
            3. View completed skills
            4. View incomplete skills
            5. View Progress
      ''')
        if int(inp) == 1:
            self.prompts()
        elif int(inp) == 2:
            self.view_all()
        elif int(inp) == 3:
            self.view_done()
        elif int(inp) == 4:
            self.view_not_done()
        elif int(inp) == 5:
            self.view_progress()
        else:
          self.welcome()


    def prompts(self):
        remind = 'Your input is incorrect try again'
        duplicate = 'That input already exists'
        upd = 'Do you want to update the condition'
        success = 'Your data has been successfully added!'
        view_all = 'Do you want to view all your skills?'
        view_done = 'To view completed skills'
        view_notdone = 'To view skills that have not been done'
        skill = input('Add your skill: ')
        skill = skill

        while skill == '':
            print(remind)
            skill = input('Add your skill: ')
        if skill:
            for key in self.skills_dict:
                while skill == key:
                    print(duplicate)
                    upd = input(upd)
                    if upd in ('y', 'yes'):
                      self.update(skill, upd)
                    else:
                      skill = input('Add your skill: ')
        while skill is None:
            print(remind)
            skill = input('Add your skill')
            progress = input('Enter `y` or `n` to signify done or not done: ')

        progress = input(
            'Enter `y` or `n` to signify done or not done: ').lower()
        while progress not in ('y', 'n', 'yes', 'no'):
            progress = input('Input has to be y or n: ')
        progress = progress
        skill.lower()

        self.add(skill, progress)
        print(success)
        exi = input('Do you want to continue adding skills?[y/n]').lower()
        while exi not in ('y', 'n'):
            exi = input('Input has to be y or n: ')
        if exi == 'n':
            self.view_all()
            print("Bye")
            leave = input('Before you leave do you want to view your data?[y/n]: ')
            if leave == 'y':
              self.view_progress()
              self.view_all()
              exit()
        else:
            self.prompts()

        print(self.getData())
        self.prompts()
        self.view_all()

    def add(self, skill, condition):
        """
        @brief Method for adding values to the global dictionary

        parameters:
                skill: the skill to work on

                condition: is it done or not
        """
        self.skills_dict[skill] = condition

    def getData(self):
        """
        @brief Method for fetching the global dictionary
        """
        return self.skills_dict

    def update(self, skill, condition):
        """
        @brief Method for updating the global dictionary

        parameters:
                skill: the skill to update

                condition: is it done or not
        """
        self.skills_dict[skill] = condition

    def view_all(self):
      if len(self.skills_dict):
          print("\nHere is a list of all the skills\n%s\n" % ('-' * 32))
          done_list = []
          not_done_list = []
          skills_list = [['Completed', 'Not completed']]
          for key, value in self.skills_dict.items():
              # print("%s: %s" %(key.title(), value.title()))
              if value.lower() == "n":
                  not_done_list.append(key.title())
              else:
                  done_list.append(key.title())

          if len(done_list) > len(not_done_list):
              for i, val in enumerate(done_list):
                  if i < len(not_done_list):
                      skills_list.append([val, not_done_list[i]])
                  else:
                      skills_list.append([val, ''])
          else:
              for i, val in enumerate(not_done_list):
                  if i < len(done_list):
                      skills_list.append([done_list[i], val])
                  else:
                      skills_list.append(['', val])

          table = AsciiTable(skills_list)
          print(table.table)
      else:
            print("\nNothing to see here :)\nNo skills have been added yet")


    def view_done(self):

        if len(self.skills_dict):
            skills_list = [['Done']]
            if "done" in [x.lower() for x in self.skills_dict.values()]:
                print("\nHere are the Skills that you have done")
                for key, value in self.skills_dict.items():
                    if value.lower() == "y":
                        skills_list.append([key.title()])
                        # print("%s: %s" %(key.title(), value.title()))
                table = AsciiTable(skills_list)
                print(table.table)
            else:
                print("\nNothing to see here :)\nYou haven't completed any skills yet")
        else:
            print("\nNothing to see here :)\nNo skills have been added yet")

    def view_not_done(self):
        if len(self.skills_dict):
            skills_list = [['n']]
            if "not done" in [x.lower() for x in self.skills_dict.values()]:
                print("\nHere are the Skills that you have not done")
                for key, value in self.skills_dict.items():
                    if value.lower() == "n":
                        skills_list.append([key.title()])
                        # print("%s: %s" %(key.title(), value.title()))
                table = AsciiTable(skills_list)
                print(table.table)
            else:
                print(
                    "\nNothing to see here :)\nLooks like you've completed all the skills!")
        else:
            print("\nNothing to see here :)\nNo skills have been added yet")
            
    
    def view_progress(self):
        if len(self.skills_dict):
            print("\nCheck out your progress\n%s" % ("-" * 23))
            done_count, not_done_count = (0, 0)
            for key, value in self.skills_dict.items():
                if value.lower() == "n":
                    not_done_count += 1
                else:
                    done_count += 1
            total_count = done_count + not_done_count
            percentage_done = int((done_count / total_count) * 100)

            print("%d%s Done (%d skills)\n%d%s Not Done (%d skills)\n" % (
                percentage_done, '%', done_count, (100 - percentage_done), '%', not_done_count))
            print("%s%s" % ("+" * (percentage_done // 4),
                            "-" * ((100 - percentage_done) // 4)))
        else:
            print("\nNothing to see here :)\nNo skills have been added yet")




    	
c = Todo()
c.welcome()
c.prompts()