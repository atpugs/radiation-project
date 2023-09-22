import { Component, Output, EventEmitter } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';

@Component({
  selector: 'app-iopanel',
  templateUrl: './iopanel.component.html',
  styleUrls: ['./iopanel.component.css']
})
export class IopanelComponent {

  @Output() public childEvent = new EventEmitter();
  effectivedose: any;
  serverData: JSON;
  ed: any = "Effective Dose: 0 µSv" ;

  constructor(private httpClient: HttpClient) { 
  }

  sayHi(lat1, lng1, lat2, lng2, alt, spd) {

    //var postData = {"src":src, "dest":dest, "dept":dept, "alt":alt, "spd":spd};

    //this.httpClient.post('http://127.0.0.1:5002/', postData).subscribe();
    
    this.httpClient.get('http://127.0.0.1:5002/', {
      params: {
        lat1: lat1,
        lng1: lng1,
        lat2: lat2,
        lng2: lng2,
        alt: alt,
        spd: spd
      }}).subscribe(data => {
      this.serverData = data as JSON;
      console.log(this.serverData[16]["nd"]);
      this.effectivedose = this.serverData[0]["ed"];
      this.serverData[1]["ed"] = lng1;
      this.serverData[2]["ed"] = lng2;
      this.childEvent.emit(this.serverData);
      this.ed = "Effective Dose:" + Math.round(this.effectivedose*100)/10 + " µSv";
    })
  }

}
