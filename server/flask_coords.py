from flask import Flask, request
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify

app = Flask(__name__)
api = Api(app)

cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)

@app.route("/", methods=['GET'])
def hello():
    parameters = request.args
        # -*- coding: utf-8 -*-
    """
    Created on Sun Sep 16 03:13:54 2018
    
    @author: Arnab Gupta
    """
    
    import math
    import csv
    
    longitude1=float(parameters['lng1'])
    latitude1=float(parameters['lat1'])
    longitude2=float(parameters['lng2'])
    latitude2=float(parameters['lat2'])
    speed=int(parameters['spd'])
    height=float(parameters['alt'])
    print(longitude1);
    print(longitude2);
    print(latitude1);
    print(latitude2);
    print(speed);
    print(height);
    '''
    longitude1=19
    longitude2=19
    latitude1=69
    latitude2=47
    speed=885.0
    height=35000
    '''
    ptlon1 = longitude1
    ptlat1 = latitude1
    ptlon2 = longitude2
    ptlat2 = latitude2
    num_of_segments=50;
    numberofsegments = num_of_segments
    onelessthansegments = numberofsegments - 1
    fractionalincrement = (1.0/onelessthansegments)
    
    ptlon1_radians = math.radians(ptlon1)
    ptlat1_radians = math.radians(ptlat1)
    ptlon2_radians = math.radians(ptlon2)
    ptlat2_radians = math.radians(ptlat2)
    
    distance_radians=2*math.asin(math.sqrt(math.pow((math.sin((ptlat1_radians-ptlat2_radians)/2)),2) + math.cos(ptlat1_radians)*math.cos(ptlat2_radians)*math.pow((math.sin((ptlon1_radians-ptlon2_radians)/2)),2)))
    # 6371.009 represents the mean radius of the earth
    # shortest path distance
    distance_km = 6371.009 * distance_radians
    
    mylats = []
    mylons = []
    
    # write the starting coordinates
    mylats.append([])
    mylons.append([])
    mylats[0] = ptlat1
    mylons[0] = ptlon1 
    
    f = fractionalincrement
    icounter = 1
    while (icounter <  onelessthansegments):
            icountmin1 = icounter - 1
            mylats.append([])
            mylons.append([])
            # f is expressed as a fraction along the route from point 1 to point 2
            A=math.sin((1-f)*distance_radians)/math.sin(distance_radians)
            B=math.sin(f*distance_radians)/math.sin(distance_radians)
            x = A*math.cos(ptlat1_radians)*math.cos(ptlon1_radians) + B*math.cos(ptlat2_radians)*math.cos(ptlon2_radians)
            y = A*math.cos(ptlat1_radians)*math.sin(ptlon1_radians) +  B*math.cos(ptlat2_radians)*math.sin(ptlon2_radians)
            z = A*math.sin(ptlat1_radians) + B*math.sin(ptlat2_radians)
            newlat=math.atan2(z,math.sqrt(math.pow(x,2)+math.pow(y,2)))
            newlon=math.atan2(y,x)
            newlat_degrees = math.degrees(newlat)
            newlon_degrees = math.degrees(newlon)
            mylats[icounter] = newlat_degrees
            mylons[icounter] = newlon_degrees
            icounter += 1
            f = f + fractionalincrement
    
    # write the ending coordinates
    mylats.append([])
    mylons.append([])
    mylats[onelessthansegments] = ptlat2
    mylons[onelessthansegments] = ptlon2
    year=2018; #edit
    date=13; #edit
    month=9; #edit
    hour=0;
    min=0;
    seconds=64200;
    geo_dist=distance_km;
    add_time=0;
    quantum=distance_km/(speed*50);
    effective_dose=0;
    sum_norm=0;
    normalized_dose=[]
    for tracker in range(num_of_segments):
        
        altitudes=[];
        densities=[];
        count=0;
        with open("altitude-density.csv", "rt", encoding="utf8") as f:
            reader = csv.reader(f)
            for row in reader:
                #print(row)
                count=count+1;
                if count>4 and count<25:
                    #print(row[0]);
                    altitudes.append(float(row[0]));
                    densities.append(float(row[4]));
                
        count=0;
        Se=[0.01];
        sp_energies=[19.8];
        
        with open("stopping_power_air.csv", "rt", encoding="utf8") as f:
            reader = csv.reader(f)
            for row in reader:
                #print(row)
                count=count+1;
                if count>1:
                    #print(row[0]);
                    sp_energies.append(float(row[0]));
                    Se.append(float(row[1]));
        
        count=0;       
        sblood=[0.01];
        S1=[22.5];
        with open("skin.csv", "rt", encoding="utf8") as f:
            reader = csv.reader(f)
            for row in reader:
                #print(row)
                count=count+1;
                if count>1:
                    #print(row[0]);
                    sblood.append(float(row[0]));
                    S1.append(float(row[1]));
            
        count=0;
        sbone=[0.01];
        S2=[20.7];
        with open("bone.csv", "rt", encoding="utf8") as f:
            reader = csv.reader(f)
            for row in reader:
                #print(row)
                count=count+1;
                if count>1:
                    #print(row[0]);
                    sbone.append(float(row[0]));
                    S2.append(float(row[1]));
                
        count=0;
        slung=[0.01];
        S3=[22.3];
        with open("lung.csv", "rt", encoding="utf8") as f:
            reader = csv.reader(f)
            for row in reader:
                #print(row)
                count=count+1;
                if count>1:
                    #print(row[0]);
                    slung.append(float(row[0]));
                    S3.append(float(row[1]));
                
    
        h=height; #edit this to actual flight height at that point
        latitude=mylats[tracker]; #edit this to actual flight latitudinal position at that point
    #    year=2018; #edit
    #    date=13; #edit
    #    month=9; #edit
        hour=19; #edit
        min=30; #edit
        time=hour*100+min;
    #    seconds=64200; #edit; seconds of the day
        L=math.radians(90-latitude)/math.pow(math.sin(math.radians(90-latitude)),2);
        p=1-(math.degrees(math.asin(math.pow((4*math.pow(L,6))-(3*math.pow(L,5)),-0.25)))/90);
    
        '''
        pos_lat=0;
        for i in range(len(latitudes)-1):
            if latitude>=latitudes[i] and latitude<=latitudes[i+1]:
                dif_l=latitude-latitude[i];
                dif_h=latitude[i+1]-latitude;
                pos_lat=i+1;
                if dif_l<dif_h:
                    pos_lat=i;
                    if latitude>=latitudes[len(latitudes)-1]:
                        pos_lat=len(latitudes)-1;
                        '''
                        
    #get closest altitude and density approximation of atmosphere
        pos_alt=0;
        for i in range(len(altitudes)-1):
            if h>=altitudes[i] and h<=altitudes[i+1]:
                dif_l=h-altitudes[i];
                dif_h=altitudes[i+1]-h;
                pos_alt=i+1;
                if dif_l<dif_h:
                    pos_alt=i;
        if h>=altitudes[len(altitudes)-1]:
            pos_alt=len(altitudes)-1;
    
    #electron flux
        count=0;
        electron_flux1=[];
        electron_flux2=[];
        electron_flux3=[];
        proton_flux1=[];
        proton_flux2=[];
        proton_flux3=[];
        proton_flux4=[];
        proton_flux5=[];
        proton_flux6=[];
        years=[];
        dates=[];
        months=[];
        times=[];
        seconds=[];
        with open("goes_electron_flux.csv", "rt") as f:
            reader = csv.reader(f)
            for row in reader:
                #print(row);
                count=count+1;
                if count>1:
                    electron_flux1.append(float(row[12]));
                    electron_flux2.append(float(row[13]));
                    electron_flux3.append(float(row[14]));
                    proton_flux1.append(float(row[6]));
                    proton_flux2.append(float(row[7]));
                    proton_flux3.append(float(row[8]));
                    proton_flux4.append(float(row[9]));
                    proton_flux5.append(float(row[10]));
                    proton_flux6.append(float(row[11]));
                    years.append(float(row[0]));
                    months.append(float(row[1]));
                    dates.append(float(row[2]));
                    times.append(float(row[3]));
                    seconds.append(float(row[5]));
                    
        pos_flux=0;
        flag=0;
        for i in range(len(electron_flux1)-1):
            #print(i);
            if years[i]==year and date==dates[i] and month==months[i] and years[i+1]==year and date==dates[i+1] and month==months[i+1]:
                if time>=times[i] and time<=times[i+1]:
                    #print(i);
                    dif_l=time-times[i];
                    dif_h=times[i+1]-time;
                    pos_flux=i+1;
                    if dif_l<dif_h:
                        pos_flux=i;
                    elif years[i]==year and date==dates[i] and month==months[i]:
                        if time>=times[i]:
                            pos_flux=i;
                            break;
                
    #Se=[1.681,1.783,1.851];
        E=[1.5,3,4];
        Sp=[10.18,53.15,22.94,13.12,8.006,6.443];
        Ep=[3,7,20,40,75,100];
        con_lambda=1; #edit to ??
        reduced_sum1e=0;
        reduced_sum2e=0;
        reduced_sum3e=0;
        tflux1e=electron_flux1[pos_flux]*p*E[0];
        #print(tflux1e)
        tflux2e=electron_flux2[pos_flux]*p*E[1];
        tflux3e=electron_flux3[pos_flux]*p*E[2];
        altitudes.append(80000);
        for i in range(pos_alt,len(altitudes)-1):
            #density=math.exp(((-9.81)*(i-11000))/(287.058*216.65))*0.365*0.001;
            pos_energy1=len(sp_energies)-1;
            pos_energy2=pos_energy1;
            pos_energy3=pos_energy2;
            for l in range(len(sp_energies)-1):
                if E[0]>=sp_energies[l] and E[0]<=sp_energies[l+1]:
                    pos_energy1=l;
            for l in range(len(sp_energies)-1):
                if E[1]>=sp_energies[l] and E[1]<=sp_energies[l+1]:
                    pos_energy2=l;
            for l in range(len(sp_energies)-1):
                if E[2]>=sp_energies[l] and E[2]<=sp_energies[l+1]:
                    pos_energy3=l;
            reduction1=(Se[pos_energy1]*densities[i]*0.1*0.001*(altitudes[i+1]-altitudes[i]));
            reduction2=(Se[pos_energy2]*densities[i]*0.1*0.001*(altitudes[i+1]-altitudes[i]));
            reduction3=(Se[pos_energy3]*densities[i]*0.1*0.001*(altitudes[i+1]-altitudes[i]));
            if E[0]==0:
                reduction1=0;
            if E[1]==0:
                reduction2=0;
            if E[2]==0:
                reduction3=0;
            E[0]=E[0]-reduction1;
            E[1]=E[1]-reduction2;
            E[2]=E[2]-reduction3;
            if E[0]<0:
                E[0]=0;
            if E[1]<0:
                E[1]=0;
            if E[2]<0:
                E[2]=0;
            reduced_sum1e=reduced_sum1e+reduction1;
            reduced_sum2e=reduced_sum2e+reduction2;
            reduced_sum3e=reduced_sum3e+reduction3;
        tflux1e=tflux1e-electron_flux1[pos_flux]*p*reduced_sum1e;
        tflux2e=tflux1e-electron_flux2[pos_flux]*p*reduced_sum1e;
        tflux3e=tflux1e-electron_flux3[pos_flux]*p*reduced_sum1e;
        E_copy=E[:];
        wt=[0.01,0.01,0.12]
        pos_energy1=len(sp_energies)-1;
        pos_energy2=pos_energy1;
        pos_energy3=pos_energy2;
        for l in range(len(sp_energies)-1):
            if E[0]>=sp_energies[l] and E[0]<=sp_energies[l+1]:
                pos_energy1=l;
        for l in range(len(sp_energies)-1):
            if E[1]>=sp_energies[l] and E[1]<=sp_energies[l+1]:
                pos_energy2=l;
        for l in range(len(sp_energies)-1):
            if E[2]>=sp_energies[l] and E[2]<=sp_energies[l+1]:
                pos_energy3=l;
        dose1=tflux1e*electron_flux1[pos_flux]*p*(S1[pos_energy1]*wt[0] + S2[pos_energy1]*wt[1] + S3[pos_energy1]*wt[2]);
    
        dose2=tflux2e*electron_flux2[pos_flux]*p*(S1[pos_energy2]*wt[0] + S2[pos_energy2]*wt[1] + S3[pos_energy2]*wt[2]);
        dose3=tflux3e*electron_flux3[pos_flux]*p*(S1[pos_energy3]*wt[0] + S2[pos_energy3]*wt[1] + S3[pos_energy3]*wt[2]);
        if dose1<0:
            dose1=0;
        if dose2<0:
            dose2=0;
        if dose3<0:
            dose3=0;
        dose=dose1+dose2+dose3;
    #/3344102498)*
        norm_dose=dose*quantum;
        normalized_dose.append(dose/3344102498.0);
        sum_norm=(dose/3344102498.0)+sum_norm;
    #    print(norm_dose)
        effective_dose=effective_dose+norm_dose;
#    return jsonify({'text': effective_dose})
    sum_norm=sum_norm/num_of_segments;
    effective_dose=effective_dose/math.pow(10,9)
    return jsonify([
            {'lat': mylats[0], 'nd': normalized_dose[0], 'ed': sum_norm}, 
            {'lat': mylats[1], 'nd': normalized_dose[1], 'ed': effective_dose},
            {'lat': mylats[2], 'nd': normalized_dose[2], 'ed': effective_dose}, 
            {'lat': mylats[3], 'nd': normalized_dose[3], 'ed': effective_dose},
            {'lat': mylats[4], 'nd': normalized_dose[4], 'ed': effective_dose}, 
            {'lat': mylats[5], 'nd': normalized_dose[5], 'ed': effective_dose},
            {'lat': mylats[6], 'nd': normalized_dose[6], 'ed': effective_dose}, 
            {'lat': mylats[7], 'nd': normalized_dose[7], 'ed': effective_dose},
            {'lat': mylats[8], 'nd': normalized_dose[8], 'ed': effective_dose}, 
            {'lat': mylats[9], 'nd': normalized_dose[9], 'ed': effective_dose},
            {'lat': mylats[10], 'nd': normalized_dose[10], 'ed': effective_dose}, 
            {'lat': mylats[11], 'nd': normalized_dose[11], 'ed': effective_dose},
            {'lat': mylats[12], 'nd': normalized_dose[12], 'ed': effective_dose}, 
            {'lat': mylats[13], 'nd': normalized_dose[13], 'ed': effective_dose},
            {'lat': mylats[14], 'nd': normalized_dose[14], 'ed': effective_dose}, 
            {'lat': mylats[15], 'nd': normalized_dose[15], 'ed': effective_dose},
            {'lat': mylats[16], 'nd': normalized_dose[16], 'ed': effective_dose}, 
            {'lat': mylats[17], 'nd': normalized_dose[17], 'ed': effective_dose},
            {'lat': mylats[18], 'nd': normalized_dose[18], 'ed': effective_dose}, 
            {'lat': mylats[19], 'nd': normalized_dose[19], 'ed': effective_dose},
            {'lat': mylats[20], 'nd': normalized_dose[20], 'ed': effective_dose},
            {'lat': mylats[21], 'nd': normalized_dose[21], 'ed': effective_dose},
            {'lat': mylats[22], 'nd': normalized_dose[22], 'ed': effective_dose}, 
            {'lat': mylats[23], 'nd': normalized_dose[23], 'ed': effective_dose},
            {'lat': mylats[24], 'nd': normalized_dose[24], 'ed': effective_dose}, 
            {'lat': mylats[25], 'nd': normalized_dose[25], 'ed': effective_dose},
            {'lat': mylats[26], 'nd': normalized_dose[26], 'ed': effective_dose}, 
            {'lat': mylats[27], 'nd': normalized_dose[27], 'ed': effective_dose},
            {'lat': mylats[28], 'nd': normalized_dose[28], 'ed': effective_dose}, 
            {'lat': mylats[29], 'nd': normalized_dose[29], 'ed': effective_dose},
            {'lat': mylats[30], 'nd': normalized_dose[30], 'ed': effective_dose},
            {'lat': mylats[31], 'nd': normalized_dose[31], 'ed': effective_dose},
            {'lat': mylats[32], 'nd': normalized_dose[32], 'ed': effective_dose}, 
            {'lat': mylats[33], 'nd': normalized_dose[33], 'ed': effective_dose},
            {'lat': mylats[34], 'nd': normalized_dose[34], 'ed': effective_dose}, 
            {'lat': mylats[35], 'nd': normalized_dose[35], 'ed': effective_dose},
            {'lat': mylats[36], 'nd': normalized_dose[36], 'ed': effective_dose}, 
            {'lat': mylats[37], 'nd': normalized_dose[37], 'ed': effective_dose},
            {'lat': mylats[38], 'nd': normalized_dose[38], 'ed': effective_dose}, 
            {'lat': mylats[39], 'nd': normalized_dose[39], 'ed': effective_dose},
            {'lat': mylats[40], 'nd': normalized_dose[40], 'ed': effective_dose},
            {'lat': mylats[41], 'nd': normalized_dose[41], 'ed': effective_dose},
            {'lat': mylats[42], 'nd': normalized_dose[42], 'ed': effective_dose}, 
            {'lat': mylats[43], 'nd': normalized_dose[43], 'ed': effective_dose},
            {'lat': mylats[44], 'nd': normalized_dose[44], 'ed': effective_dose}, 
            {'lat': mylats[45], 'nd': normalized_dose[45], 'ed': effective_dose},
            {'lat': mylats[46], 'nd': normalized_dose[46], 'ed': effective_dose}, 
            {'lat': mylats[47], 'nd': normalized_dose[47], 'ed': effective_dose},
            {'lat': mylats[48], 'nd': normalized_dose[48], 'ed': effective_dose}, 
            {'lat': mylats[49], 'nd': normalized_dose[49], 'ed': effective_dose}  
            ])
    #print(sum_norm/num_of_segments);
    #print(effective_dose);   


if __name__ == '__main__':
     app.run(port=5002)