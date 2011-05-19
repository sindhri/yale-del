root=File.expand_path(Dir.pwd)
puts ">>> Serving: #{root}"

app = Rack::Builder.app do  
  map "/labs/del" do
    run Rack::Directory.new("#{root}/www")
  end
end

run app