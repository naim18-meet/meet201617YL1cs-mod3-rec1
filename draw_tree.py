from branch import Branch
import turtle

max_depth=7 #The maximum number of branches the tree can have
length=256 #The length of the first branch
startx=0
starty=-250
branch1=Branch((startx,starty),(startx,starty+length))
turtle.hideturtle()

def draw_tree( this_branch, branch_num ):
    '''
    Draw a branch in the tree; then, split the branch and
    recursively call draw_tree again.

    :param this_branch: the branch that will be drawn in turtle
    :param branch_num: the number corresponding to how deep in the tree this branch exists
    '''
    #Complete this method
    turtle.penup()
    turtle.goto(this_branch.start)
    turtle.pendown()
    turtle.goto(this_branch.stop)
    if(branch_num > max_depth):
        pass
    else:
        branch_num=branch_num+1
        Branches = this_branch.split()

        for i in Branches:
            draw_tree(1,branch_num)
            

draw_tree(branch1,1)


turtle.mainloop()
