import os
# ------------->>        CREATING A PARTITION       <<--------

def create_partition():
    print("\t\t YOU HAVE CHOSEN DISK PARTITION OPTION \n\n")
    d = input("Enter the Disk Name: ")
    ps = input("Enter the Partition Size: ")
    i = "(echo 'n' ; echo 'p' ; echo -ne '\n' ; echo -ne '\n' ; echo '+'+ps+'G';) | fdisk /dev/"+d
    os.system(i)
    os.system("udevadm settle")
    os.system("lsblk")

# -------------->>         formatting a disk        <<-------


def format_disk():
    d = input("Enter disk name")
    os.system("mkfs.ext4 /dev/"+d)

# ------------->>   To mount a disk                 <<-------


def mount_disk():
    f = input("Enter disk name: ")
    p = input("Enter a participation name(example drive3): ")
    os.system("mkdir /"+p)
    os.system("lsblk")
    os.system("mount /dev/"+f + " " + "/"+p)
    os.system("cd /"+p)
    os.system("lsblk")


# -------------->>         formatting a disk        <<-------

def format_disk():
    d = input("Enter disk name")
    os.system("mkfs.ext4 /dev/"+d)

# ------------->>   To mount a disk                 <<-------


def mount_disk():
    f = input("Enter disk name: ")
    p = input("Enter a participation name(example drive3): ")
    os.system("mkdir /"+p)
    os.system("lsblk")
    os.system("mount /dev/"+f + " " + "/"+p)
    os.system("cd /"+p)
    os.system("lsblk")


# ------------->>   To configure yum                <<-------

def configure_yum():
    os.system("cd /etc/yum.repos.d")
    f1 = open("yum1.repo", "w")
    f1.write('''
[dvd1]
baseurl=/run/media/root/RHEL-8-0-0-BaseOS-x86_64/AppStream
gpgcheck=0

[dvd2]
baseurl=/run/media/root/RHEL-8-0-0-BaseOS-x86_64/BaseOS
gpgcheck=0''')
    f1.close()
    loc = input(
        "Enter the director name where your menu Program is save (/arth/menu.py: ")
    os.system("cp "+loc+"/yum1.repo /etc/yum.repos.d")
    os.system(
        "dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm -y")


# ------------->>   To configure apache web server  <<-------

def configure_appache_web_server():
    os.system("dnf install httpd -y")
    os.system("systemctl enable httpd")


# ------------->>   To create a Lvm Storage         <<-------


def create_lvm_storage():
    d1 = input("Enter first disk name: ")
    d2 = input("Enter second disk name: ")
    v = input("Enter the name of the volume group: ")
    n = input("Enter the name of the LVM: ")
    s = input("Enter the size of the LVM: ")
    dr = input("Input the LVM mountpoint name i.e Create a Directory: ")
    # pv creation
    os.system("pvcreate /dev/"+d1)
    os.system("pvcreate /dev/"+d2)
    # vg creation
    os.system("vgcreate "+v+" /dev/"+d1+" /dev/"+d2)
    os.system("vgdisplay "+v)
    # lvm creation
    os.system("lvcreate --size +"+s+"G --name "+n+" "+v)
    # formatting
    os.system("mkfs.ext4 /dev/"+v+"/"+n)
    # mounting
    os.system("mkdir /"+dr)
    os.system("mount /dev/"+v+"/"+n+" "+"/"+dr)
    os.system("cd /"+dr)


# ------------->>   To create a namenode on hadoop  <<-------


def create_namenode_hadoop():
    os.system("hadoop namenode -format")
    os.system("cd /etc/hadoop")
    os.system("rm -rf hdfs-site.xml")
    os.system("rm -rf core-site.xml")
    ipm = input("Input master IP: ")
    dir2 = input("Name your directory you want to create and use: ")
    os.system("mkdir /"+dir2)
    os.system("cd /etc/hadoop")
    f2 = open("/etc/hadoop/hdfs-site.xml", "w")
    f2.write('''
<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->
<configuration>
<property>
<name>dfs.name.dir</name>
<value>/{}</value>
</property>
</configuration>'''.format(dir2))
    f2.close()
    os.system("systemctl disable firewalld")
    os.system("systemctl stop firewalld")
    f3 = open("/etc/hadoop/core-site.xml", "w")
    f3.write("""
<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{}</value>

</property>
</configuration>""".format(ipm))
    f3.close()
    os.system("hadoop-daemon.sh start namenode")


# ------------->>   To create a datanode on hadoop  <<-------

def create_datanode_hadoop():
    os.system("cd /etc/hadoop")
    os.system("rm -rf hdfs-site.xml")
    os.system("rm -rf core-site.xml")
    dir2 = input("Name your directory you want to create and use: ")
    os.system("mkdir /"+dir2)
    ipm = input("Please enter the Ip of master You want to connect with: ")
    f4 = open("/etc/hadoop/hdfs-site.xml", "w")
    f4.write('''
<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->
<configuration>
<property>
<name>dfs.data.dir</name>
<value>/{}</value>
</property>
</configuration>'''.format(dir2))
    f4.close()
    f5 = open("/etc/hadoop/core-site.xml", "w")
    f5.write("""
<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{}</value>

</property>
</configuration>""".format(ipm))
    f5.close()
    os.system("systemctl disable firewalld")
    os.system("systemctl stop firewalld")
    os.system("hadoop-daemon.sh start datanode")


# ------------->>   To create a client on hadoop    <<-------

def create_hadoop_client():
    os.system("systemctl stop firewalld")
    os.system("systemctl disable firewalld")
    ipm = input("Please enter the Ip of master You want to connect with: ")
    f5 = open("/etc/hadoop/core-site.xml", "w")
    f5.write('''
<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{}</value>

</property>
</configuration>'''.format(ipm))
    f5.close()


# ------------->>   To Install Hadoop on the system <<-------

def install_hadoop():
    pre = input("Do you have the hadoop rpm downloaded already?(y/n): ")
    if(pre == "n"):
        print("Can't he;p you directly")
    else:
        y = input("Input the full-directory where rpm is downloaded/saved")
        os.system(y)
        os.system("yum install -y java-1.8.0-openjdk")
        os.system("rpm -ivh hadoop-1.2.1-1.x86_64 --force")
