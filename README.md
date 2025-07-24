# Replication package of the paper "A Taxonomy of System-Level Attacks on Deep Learning Models in Autonomous Vehicles"


- The **ChatGPT_for_AVs.pdf** file is the ChatGPT search for finding the domains of Autonomous Vehicles, Deep Learning models and modules, and simulation environment.

# How to Replicate:
1. Install <a href="https://github.com/jonatasgrosman/findpapers">findpapers</a> by using ``pip install findpapers``.
2. Find our query from the **send_query.py**. Copy it and run it to find and extract the papers.
3. Change the ``json_dir_path = './findpapers'`` in the **venue_filter.py** to the direction of your outputed list of papers.
4. Run the **venue_filter.py** to filter venues based on the listed venues in **chosen_venues.txt** file.
5. You will have a **papers_after_venue_filter.csv** which contains the title, abstract, URLs, venue, and published date of the papers.

- Note: The **venue_freq.py** file outputs the number of papers extracted from each venue, separated by journals and conferences. You can skip running this code, as it was only intended for us to find related venues.

# Citation 
If you find this taxonomy useful, please consider giving it a star &#127775;, and cite the published paper:
[https://arxiv.org/abs/2503.09385](https://arxiv.org/abs/2412.04510)
```bibtex
@article{tehrani2024taxonomy,
  title={A Taxonomy of System-Level Attacks on Deep Learning Models in Autonomous Vehicles},
  author={Tehrani, Masoud Jamshidiyan and Kim, Jinhan and Foulefack, Rosmael Zidane Lekeufack and Marchetto, Alessandro and Tonella, Paolo},
  journal={arXiv preprint arXiv:2412.04510},
  year={2024}
}
