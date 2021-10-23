#!/bin/bash
echo ${1}

git_push(){
	echo "开始push"
	modify_time=`stat -c %Y ${1}`
	this_time=`date +%s`

	cd ${1}
	echo "-------切换目录------"
	echo `pwd`
	echo "---------------------"
#	echo  [$[ ${modify_time}-${this_time} ] -gt 86400 ] 
#	if [ $[ ${modify_time}-${this_time} ] -gt 86400 ];
#	then
	echo "${1} 文件夹 有变化，正在准备push..."
	date=`date "+%Y-%m-%d %H:%M:%S"`
	git add .    
	git commit -m "automatic push @$(date)"
	echo "git fetch origin master"
	git fetch origin master

	echo "git merge origin/master"
	git merge origin/master

	echo "git push origin master:master"
	git push origin master:master

#	fi
}

git_push /home/lhy/codes/offer

