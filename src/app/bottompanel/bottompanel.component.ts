import { Component, OnInit, Input, ViewChild } from '@angular/core';
import { trigger, state, style, transition, animate} from '@angular/animations';

@Component({
  selector: 'app-bottompanel',
  templateUrl: './bottompanel.component.html',
  styleUrls: ['./bottompanel.component.css'],
  animations: [
    trigger('slideInOut', [
      state('out', style({
        transform: 'translate3d(0, 0, 0)'
      })),
      state('in', style({
        transform: 'translate3d(0, 100%, 0)'
      })),
      transition('in => out', animate('500ms ease-in-out')),
      transition('out => in', animate('500ms ease-in-out'))
    ]),
  ]
})

export class BottompanelComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  } 
  
  @Input('parentData') public serverData;

  public lineChartLabels:Array<any> = null;
  public lineChartData:Array<any> =  null;
  public i: number = 0;
  ed: number = 0;
  banana: number = 0;
  public lineChartType: string = 'line';

  menuState: string = "in";
  public visibility: string = "visible";

  toggleBottomPanel() {
    this.menuState = this.menuState === 'out' ? 'in' : 'out';
    if(this.serverData != null)
    {
      this.ed = parseFloat(this.serverData[0]["ed"]);
      this.banana = this.ed*100;
      this.banana = Math.round(this.banana);
      this.ed = Math.round(this.ed);

      for(this.i=0;this.i<50;this.i++)
      {
        this.lineChartLabels[0]["data"][this.i] = parseFloat(this.serverData[this.i]["lat"]);
        this.lineChartData[0]["data"][this.i]  = parseFloat(this.serverData[this.i]["nd"]);
      }
    }
  }

  toggleToggleVisibility() {
    this.visibility = this.visibility === 'visible' ? 'hidden' : 'visible';
  }
  setToggleVisibility(vis) {
    this.visibility = vis;
  }
}
