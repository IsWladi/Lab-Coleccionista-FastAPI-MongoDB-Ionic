import { Component, OnInit } from '@angular/core';
import { ExamplesService } from '../api/examples.service';

@Component({
  selector: 'app-tab1',
  templateUrl: 'tab1.page.html',
  styleUrls: ['tab1.page.scss'],
})
export class Tab1Page implements OnInit {
  constructor(private apiService: ExamplesService) {
  }

  ngOnInit() {
    this.apiService.getAllUsersWithoutAuth();
  }
  //
}
